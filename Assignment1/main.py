# main.py

import pandas as pd
from fetcher import fetch_top_rated_movies, fetch_genre_mapping
from processor import simplify_movie_data
from config import TOTAL_PAGES
from time import sleep

all_movies = []
genre_map = fetch_genre_mapping()

for page in range(1, TOTAL_PAGES + 1):
    print(f"Fetching page {page}/{TOTAL_PAGES}...")
    try:
        raw_movies = fetch_top_rated_movies(page)
        processed_movies = simplify_movie_data(raw_movies, genre_map)
        all_movies.extend(processed_movies)
        sleep(0.25)  # Prevent hitting API rate limits
    except Exception as e:
        print(f"❌ Error on page {page}: {e}")
        continue

df = pd.DataFrame(all_movies)
df.to_csv("tmdb_top_rated_movies.csv", index=False)
print("✅ Dataset saved as tmdb_top_rated_movies.csv")
