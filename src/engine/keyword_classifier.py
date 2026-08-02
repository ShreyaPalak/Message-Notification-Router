class KeywordClassifier:

    def predict(
        self,
        text,
        features,
    ):

        text = str(text).lower()

        if (
            "meeting" in text
            or "deadline" in text
        ):
            return {
                "action": "notify",
                "message_type": "work_chat",
                "reason": "Work-related content detected.",
                "confidence": 0.82,
            }

        if (
            "homework" in text
            or "exam" in text
        ):
            return {
                "action": "notify",
                "message_type": "school_update",
                "reason": "School-related content detected.",
                "confidence": 0.81,
            }

        if features["is_group"]:
            return {
                "action": "digest",
                "message_type": "society_notice",
                "reason": "Group communication detected.",
                "confidence": 0.72,
            }

        return {
            "action": "digest",
            "message_type": "personal_chat",
            "reason": "Default classification applied.",
            "confidence": 0.70,
        }