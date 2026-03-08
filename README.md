# Spotify Playlist Data Pipeline

## Project Overview

This project implements a **mini data pipeline** to process playlist track data. The pipeline extracts playlist metadata from a public JSON dataset, performs basic data transformations using **Pandas**, and stores the processed data locally for analysis.

The pipeline follows an **ETL (Extract–Transform–Load) architecture** and is orchestrated using **Apache Airflow** while running inside **Docker containers**.

### Pipeline Workflow

Extract → Transform → Load

1. **Extract** playlist data from an external JSON dataset.
2. **Transform** the dataset using Pandas.
3. **Load** the processed data into CSV files.

---

## Dataset Source

The playlist data is fetched from the following public JSON dataset:

https://raw.githubusercontent.com/rushi4git/spotify-playlist-data/refs/heads/main/spotify_playlist.json

The dataset contains metadata for multiple tracks including:

* track_name
* artist_name
* album_name
* popularity
* duration_ms
* release_date

---

## Technologies Used

* Python
* Pandas
* Requests
* Apache Airflow
* Docker
* Docker Compose

---

## Project Structure

```
spotify-playlist-data-pipeline
│
├── airflow
│   ├── dags
│   │   └── playlist_pipeline_dag.py
│   ├── logs
│   ├── src
│       ├── extract.py
│       ├── transform.py
│       └── load.py
│       └── output
│          ├── playlist_raw.csv
│          └── playlist_transformed.csv
│
├── docker-compose.yml
├── Dockerfile
├── main.py
├── requirements.txt
└── README.md
```

---

## Data Transformation

The following transformations are applied using **Pandas**:

### 1. Convert duration

Duration is converted from milliseconds to minutes.

```
duration_minutes = duration_ms / 60000
```

### 2. Extract release year

Extract the year from the release date.

### 3. Remove duplicate tracks

### 4. Handle missing values

### 5. Popularity Category

Tracks are categorized based on popularity:

| Popularity Range | Category |
| ---------------- | -------- |
| 0 – 40           | Low      |
| 41 – 70          | Medium   |
| 71 – 100         | High     |

---

## Steps to Run the Project

### 1. Clone the repository

```
git clone <repository-url>
cd spotify-playlist-data-pipeline
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Start Airflow using Docker

```
docker compose up
```

### 4. Open Airflow UI

Open your browser and go to:

```
http://localhost:8082
```

Login credentials:

```
Username: admin
Password: S9rhCTCQxar4Ddgx
```

### 5. Run the pipeline

1. Enable the DAG **playlist_pipeline**
2. Click **Trigger DAG**

---

## Example Output

After running the pipeline, the following files will be generated:

```
airflow/output/
   playlist_raw.csv
   playlist_transformed.csv
```

### Example Columns

```
track_name
artist_name
album_name
popularity
duration_ms
duration_minutes
release_date
release_year
popularity_category
```

---

## Conclusion

This project demonstrates a simple **data engineering pipeline** built using Python, Apache Airflow, and Docker. It shows how raw JSON data can be extracted, transformed, and stored in structured formats for analysis.
