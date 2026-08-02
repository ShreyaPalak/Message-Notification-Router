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
    evidence=None,
):

        try:

            if evidence is None:
                evidence = self.retriever.retrieve(
                    text=text,
                top_k=5,
            )

            result = self.rules.predict(text)

            if result is None:

                result = self.classifier.predict(
                    text,
                    features,
                )

            result = self.validator.validate(
                result
            )

            result["evidence_message_ids"] = (
                "|".join(map(str, evidence))
                if evidence
                else "none"
            )

            return result

        except Exception:

            return dict(FALLBACK)