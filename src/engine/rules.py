import re


class RuleEngine:

    def predict(self, text):

        text = str(text).lower()

        if re.search(r"\botp\b", text):
            return {
                "action": "notify",
                "message_type": "transactional_alert",
                "reason": "OTP detected.",
                "confidence": 0.98,
            }

        if any(
            word in text
            for word in [
                "debited",
                "credited",
                "transaction",
                "payment",
            ]
        ):
            return {
                "action": "notify",
                "message_type": "transactional_alert",
                "reason": "Transaction alert detected.",
                "confidence": 0.95,
            }

        if any(
            word in text
            for word in [
                "offer",
                "discount",
                "limited time",
                "buy now",
            ]
        ):
            return {
                "action": "mute",
                "message_type": "marketing_promo",
                "reason": "Promotional content detected.",
                "confidence": 0.90,
            }

        return {
            "action": "digest",
            "message_type": "personal_chat",
            "reason": "No high-priority indicators found.",
            "confidence": 0.70,
        }