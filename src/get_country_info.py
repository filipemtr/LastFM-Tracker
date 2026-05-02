import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("CLIENT_KEY")

def country_artists(country: str):

    params = {
        "method": "geo.gettopartists",
        "country": country,
        "api_key": API_KEY,
        "format": "json",
        "limit": 50
    }

    response = requests.get(f"http://ws.audioscrobbler.com/2.0/", params=params)
    content = response.json()["topartists"]["artist"]

    templist = []
    for artist in content:
        templist.append(artist["name"])
    
    return templist

def country_tracks(country: str):

    params = {
        "method": "geo.gettoptracks",
        "country": country,
        "api_key": API_KEY,
        "format": "json",
        "limit": 50
    }

    response = requests.get(f"http://ws.audioscrobbler.com/2.0/", params=params)
    content = response.json()["tracks"]["track"]

    templist = []
    for track in content:
        templist.append([track["name"], track["artist"]["name"]])

    return templist