from src.guardrails.fallback import FALLBACK

class Orchestrator:

    def __init__(
        self,
        rules,
        classifier,
        validator,
        retriever,
    ):
        self.rules = rules
        self.classifier = classifier
        self.validator = validator
        self.retriever = retriever

    def predict(
        self,
        row,
        text,
        features,
    ):

        try:

            evidence = self.retriever.retrieve(
                row["user_id"],
                text,
            )

            result = self.rules.predict(
                text,
            )

            if result is None:

                result = self.classifier.predict(
                    text,
                    features,
                )

            result = self.validator.validate(
                result
            )

            result["evidence_message_ids"] = (
                "|".join(evidence)
                if evidence
                else "none"
            )

            return result

        except Exception:

            return dict(FALLBACK)