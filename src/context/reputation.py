from pathlib import Path

import pandas as pd


class ReputationEngine:

    def __init__(
        self,
        business_accounts_path,
        history_path,
    ):
        self.business = self._load_csv(
            business_accounts_path
        )

        self.history = self._load_csv(
            history_path
        )

    def _load_csv(self, path):

        path = Path(path)

        if not path.exists():
            return pd.DataFrame()

        return pd.read_csv(path)

    def sender_score(
        self,
        sender_id,
    ):
        score = 0.50

        if self.business.empty:
            return score

        if "business_id" not in self.business:
            return score

        sender = self.business[
            self.business["business_id"] == sender_id
        ]

        if sender.empty:
            return score

        if "verified" in sender.columns:

            value = sender.iloc[0]["verified"]

            if bool(value):
                score += 0.25

        if "spam_score" in sender.columns:

            spam = float(
                sender.iloc[0]["spam_score"]
            )

            score -= spam

        return max(
            0.0,
            min(
                score,
                1.0,
            ),
        )