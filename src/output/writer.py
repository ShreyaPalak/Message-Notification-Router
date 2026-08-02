import pandas as pd

from src.output.validator import OutputValidator


def write_output(rows, path):

    df = pd.DataFrame(rows)

    validator = OutputValidator()

    validator.validate(df)

    columns = [
        "message_id",
        "action",
        "message_type",
        "reason",
        "confidence",
        "evidence_message_ids",
    ]

    df = df[columns]

    df.to_csv(path, index=False)