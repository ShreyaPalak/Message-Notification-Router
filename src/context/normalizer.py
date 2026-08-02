from src.context.schema import COLUMN_MAP

def normalize(df):
    return df.rename(columns=COLUMN_MAP)