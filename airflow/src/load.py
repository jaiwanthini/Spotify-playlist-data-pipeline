import os
import pandas as pd


def save_raw(df):
    output_dir = "/opt/airflow/src/output"
    os.makedirs(output_dir, exist_ok=True)
    df.to_csv(f"{output_dir}/playlist_raw.csv", index=False)


def save_transformed(df):
    output_dir = "/opt/airflow/src/output"
    os.makedirs(output_dir, exist_ok=True)
    df.to_csv(f"{output_dir}/playlist_transformed.csv", index=False)
