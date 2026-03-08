import requests
import pandas as pd

URL = "https://raw.githubusercontent.com/rushi4git/spotify-playlist-data/refs/heads/main/spotify_playlist.json"

def fetch_playlist_data():

    response = requests.get(URL)

    data = response.json()

    df = pd.DataFrame(data["tracks"])

    return df
