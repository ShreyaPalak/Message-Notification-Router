from src.guardrails.enums import (
    VALID_ACTIONS,
    VALID_TYPES,
)


class Validator:

    def validate(self, prediction):

        if prediction["action"] not in VALID_ACTIONS:
            prediction["action"] = "digest"

        if prediction["message_type"] not in VALID_TYPES:
            prediction["message_type"] = (
                "personal_chat"
            )

        prediction["confidence"] = max(
            0.0,
            min(
                float(prediction["confidence"]),
                1.0,
            ),
        )

        return prediction