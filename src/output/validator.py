import pandas as pd


class OutputValidator:

    REQUIRED_COLUMNS = [
        "message_id",
        "action",
        "message_type",
        "reason",
        "confidence",
        "evidence_message_ids",
    ]

    def validate(self, df):

        missing = set(self.REQUIRED_COLUMNS) - set(df.columns)

        if missing:
            raise ValueError(
                f"Missing columns: {missing}"
            )

        if len(df["message_id"]) != len(
            df["message_id"].unique()
        ):
            raise ValueError(
                "Duplicate message IDs detected."
            )

        return True