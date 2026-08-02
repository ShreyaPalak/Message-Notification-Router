class LLMClassifier:

    def predict(self, *args, **kwargs):

        return {
            "action": "digest",
            "message_type": "personal_chat",
            "reason": "LLM layer disabled.",
            "confidence": 0.60,
        }