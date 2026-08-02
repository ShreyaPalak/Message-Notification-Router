class FeatureBuilder:

    def build(self, row, user_row):

        opened = user_row.get(
            "messages_opened_30d",
            0,
        )

        replied = user_row.get(
            "messages_replied_30d",
            0,
        )

        dismissed = user_row.get(
            "notifications_dismissed_30d",
            0,
        )

        denominator = max(opened + dismissed, 1)

        return {
            "is_group": (
                row.get("chat_type") == "group"
            ),
            "is_forwarded": (
                row.get("forwarded_count", 0) > 2
            ),
            "open_rate": opened / denominator,
            "reply_rate": replied / denominator,
            "dismissal_rate": dismissed / denominator,
        }