import pandas as pd

from src.config import (
    MESSAGES_FILE,
    USERS_FILE,
    MESSAGE_HISTORY_FILE,
    OUTPUT_FILE,
)

from src.context.normalizer import normalize
from src.context.feature_builder import FeatureBuilder
from src.context.evidence_retriever import EvidenceRetriever

from src.engine.rules import RuleEngine
from src.engine.keyword_classifier import KeywordClassifier
from src.engine.orchestrator import Orchestrator

from src.guardrails.validation import Validator

from src.output.writer import write_output

from src.logger import log


def load_data():
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

        user_rows = users[
            users["user_id"] == row["user_id"]
        ]

        if len(user_rows):
            user_row = user_rows.iloc[0]
        else:
            user_row = {}

        text = str(row.get("text", ""))

        if text.lower() == "nan":
            text = ""

        features = feature_builder.build(
            row,
            user_row,
        )

        result = orchestrator.predict(
            row=row,
            text=text,
            features=features,
        )

        result["message_id"] = row["message_id"]

        rows.append(result)

    write_output(rows, OUTPUT_FILE)

    log("Finished execution.")
    log(f"Processed {len(rows)} messages.")

    print("Done.")


if __name__ == "__main__":
    main()