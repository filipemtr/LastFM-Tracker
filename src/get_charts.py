import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("CLIENT_KEY")


def extract_artists():
    # Extract the more listened artists from Last.Fm's charts.

    charts = requests.get(f"http://ws.audioscrobbler.com/2.0/?method=chart.gettopartists&api_key={API_KEY}&format=json")
    artists = charts.json()["artists"]["artist"]

    artists_info = []
    for artist in artists:
        artists_info.append([artist["name"], artist["listeners"], artist["playcount"]])
    
    return artists_info



def extract_genders():
    # Extract the more listened genders from Last.Fm's charts.

    tags = requests.get(f"http://ws.audioscrobbler.com/2.0/?method=chart.gettoptags&api_key={API_KEY}&format=json")
    genders = tags.json()["tags"]["tag"]

    genders_info = []
    for gender in genders:
        genders_info.append(gender["name"])
    
    return genders_info



def extract_tracks():
    # Extract the more listened musics and their artists from Last.Fm's charts.

    charts = requests.get(f"http://ws.audioscrobbler.com/2.0/?method=chart.gettoptracks&api_key={API_KEY}&format=json")
    tracks = charts.json()["tracks"]["track"]

    tracks_info = []
    for track in tracks:
        tracks_info.append([track["name"], track["playcount"], track["artist"]["name"]])

    return tracks_info

    



