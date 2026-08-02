from pathlib import Path

import pandas as pd


class GroupContext:

    def __init__(self, groups_path):

        groups_path = Path(groups_path)

        if groups_path.exists():
            self.groups = pd.read_csv(groups_path)
        else:
            self.groups = pd.DataFrame()

    def is_muted(self, group_id):

        if self.groups.empty:
            return False

        if group_id is None:
            return False

        if "group_id" not in self.groups.columns:
            return False

        group = self.groups[
            self.groups["group_id"] == group_id
        ]

        if group.empty:
            return False

        muted_columns = [
            "muted",
            "is_muted",
            "mute_status",
        ]

        for column in muted_columns:

            if column in group.columns:

                value = group.iloc[0][column]

                if bool(value):
                    return True

        return False