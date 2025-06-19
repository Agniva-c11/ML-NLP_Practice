# processor.py

def simplify_movie_data(movies, genre_map):
    simplified = []
    for movie in movies:
        simplified.append({
            "title": movie.get("title"),
            "description": movie.get("overview"),
            "genres": [genre_map.get(genre_id, "Unknown") for genre_id in movie.get("genre_ids", [])]
        })
    return simplified
