# fetcher.py

import requests
from config import API_KEY, BASE_URL, LANGUAGE
from time import sleep

def fetch_top_rated_movies(page):
    url = f"{BASE_URL}/movie/top_rated"
    params = {
        "api_key": API_KEY,
        "language": LANGUAGE,
        "page": page
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json().get("results", [])

def fetch_genre_mapping():
    url = f"{BASE_URL}/genre/movie/list"
    params = {
        "api_key": API_KEY,
        "language": LANGUAGE
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    genres = response.json().get("genres", [])
    return {genre["id"]: genre["name"] for genre in genres}
