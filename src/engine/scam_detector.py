class ScamDetector:

    def __init__(self):

        self.keywords = {
            "otp",
            "kyc",
            "lottery",
            "winner",
            "urgent",
            "claim",
            "verify",
            "account blocked",
            "click here",
            "bank account",
            "gift card",
            "upi",
            "payment link",
            "limited offer",
            "congratulations",
        }

    def predict(self, text):

        if not text:
            return None

        text = str(text).lower()

        matches = [
            keyword
            for keyword in self.keywords
            if keyword in text
        ]

        if not matches:
            return None

        return {
            "action": "mute",
            "message_type": "scam_spam",
            "reason": (
                "Message contains suspicious scam-related keywords."
            ),
            "confidence": 0.90,
            "evidence_message_ids": "none",
        }