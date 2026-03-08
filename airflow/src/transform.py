import pandas as pd

def transform_data(df):

    df["duration_minutes"] = df["duration_ms"] / 60000

    df["release_year"] = pd.to_datetime(df["release_date"]).dt.year

    df = df.drop_duplicates()

    df = df.fillna("Unknown")

    def category(p):

        if p <= 40:
            return "Low"
        elif p <= 70:
            return "Medium"
        else:
            return "High"

    df["popularity_category"] = df["popularity"].apply(category)

    return df