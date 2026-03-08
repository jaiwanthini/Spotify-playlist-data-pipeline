from src.extract import fetch_playlist_data
from src.transform import transform_data
from src.load import save_raw, save_transformed


def run_pipeline():

    df = fetch_playlist_data()

    save_raw(df)

    df_transformed = transform_data(df)

    save_transformed(df_transformed)

    print("Pipeline executed successfully")


if __name__ == "__main__":
    run_pipeline()
