import pandas as pd

from src.context.group_context import GroupContext

from src.config import (
    BUSINESS_ACCOUNTS_FILE,
    MESSAGES_FILE,
    GROUPS_FILE,
    MESSAGE_HISTORY_FILE,
    OUTPUT_FILE,
    USER_BUSINESS_HISTORY_FILE,
    USERS_FILE,
)

from src.context.normalizer import normalize
from src.context.feature_builder import FeatureBuilder
from src.context.evidence_retriever import EvidenceRetriever
from src.context.reputation import ReputationEngine

from src.engine.rules import RuleEngine
from src.engine.keyword_classifier import KeywordClassifier
from src.engine.orchestrator import Orchestrator

from src.guardrails.validation import Validator

from src.output.writer import write_output

from src.logger import log


def load_data():
    """Load all required datasets."""

    messages = pd.read_csv(MESSAGES_FILE)
    users = pd.read_csv(USERS_FILE)
    history = pd.read_csv(MESSAGE_HISTORY_FILE)

    return messages, users, history


def main():

    log("Loading datasets.")

    messages, users, history = load_data()

    messages = normalize(messages)

    feature_builder = FeatureBuilder()

    evidence_retriever = EvidenceRetriever(
        history=history
    )

    reputation_engine = ReputationEngine(
        BUSINESS_ACCOUNTS_FILE,
        USER_BUSINESS_HISTORY_FILE,
    )

    group_context = GroupContext(
        GROUPS_FILE
    )

    rules = RuleEngine()

    classifier = KeywordClassifier()

    validator = Validator()

    orchestrator = Orchestrator(
        rules=rules,
        classifier=classifier,
        validator=validator,
        retriever=evidence_retriever,
    )

    rows = []

    log("Starting message processing.")

    for _, row in messages.iterrows():

        # -------------------------------------------------
        # Locate the user
        # -------------------------------------------------

        user_rows = users[
            users["user_id"] == row["user_id"]
        ]

        if len(user_rows):
            user_row = user_rows.iloc[0]
        else:
            user_row = {}

        # -------------------------------------------------
        # Extract text
        # -------------------------------------------------

        text = str(row.get("text", ""))

        if text.lower() == "nan":
            text = ""

        # -------------------------------------------------
        # Build features
        # -------------------------------------------------

        features = feature_builder.build(
            row,
            user_row,
        )
        evidence = evidence_retriever.retrieve(
            text=text,
            top_k=5,
            )

        # -------------------------------------------------
        # Reputation scoring
        # -------------------------------------------------

        sender_id = row.get("business_id")

        score = reputation_engine.sender_score(
            sender_id
        )
        
        forwarded_count = row.get(
            "forwarded_count",
            0,)

        if pd.isna(forwarded_count):
            forwarded_count = 0

        if not pd.isna(forwarded_count):
            forwarded_count = int(forwarded_count)

        group_id = row.get("group_id")
        
        if forwarded_count >= 10:
            result = {
                "action": "mute",
                "message_type": "scam_spam",
                "reason": (
                    "Message has been heavily forwarded."
                ),
                "confidence": 0.95,
                "evidence_message_ids": "none",
                }

        elif group_context.is_muted(group_id):

            result = {
                "action": "mute",
                "message_type": "group_chat",
                "reason": (
                "Message originated from a muted group."
            ),
                "confidence": 1.0,
                "evidence_message_ids": "none",
            }

        # -------------------------------------------------
        # Hard rules
        # -------------------------------------------------

        elif score < 0.20:

            result = {
                "action": "mute",
                "message_type": "scam_spam",
                "reason": (
                    "Sender has a low reputation score."
                ),
                "confidence": 0.90,
                "evidence_message_ids": "none",
            }

        elif score > 0.80:

            result = {
                "action": "notify",
                "message_type": "transactional_alert",
                "reason": (
                    "Sender has a high reputation score."
                ),
                "confidence": 0.85,
                "evidence_message_ids": "none",
            }

        else:

            result = orchestrator.predict(
                row=row,
                text=text,
                features=features,
                evidence=evidence,
            )

        # -------------------------------------------------
        # Store results
        # -------------------------------------------------

        result["message_id"] = row["message_id"]

        
        if evidence:
            result["evidence_message_ids"] = "|".join(
        map(str, evidence)
    )
        else:
            result["evidence_message_ids"] = "none"
            
        rows.append(result)

    # -----------------------------------------------------
    # Write output
    # -----------------------------------------------------

    write_output(rows, OUTPUT_FILE)

    log("Finished execution.")
    log(f"Processed {len(rows)} messages.")

    print("Done.")


if __name__ == "__main__":
    main()