from fastapi import APIRouter, Query, Depends
from models.schemas import Movie
from routers.helper import read_json, write_json

router = APIRouter()

MOVIES_FILE = "json_files/movies.json"

# Getting all movies
@router.get("/movies")
def get_movies():
    try:
        return read_json(MOVIES_FILE)
    except Exception as e:
        return e

# Adding a new movie
@router.post("/movies")
def add_new_movie(movie : Movie):
    all_movies = read_json(MOVIES_FILE)
    all_movies.append(movie.dict())
    write_json(MOVIES_FILE, all_movies)
    return movie


# Search by genre
@router.get("/movies/genre")
def get_movies(genre: str = Query(None)):
    all_movies = read_json(MOVIES_FILE)
    if genre:
        filtered_movies = []
        target_genre = genre.lower()
        for movie in all_movies:
            if movie["genre"].lower() == target_genre:
                filtered_movies.append(movie)
        all_movies = filtered_movies
    return all_movies


# Search by rating
@router.get("/movies/rating")
def get_movies(rating: float = Query(None)):
    all_movies = read_json(MOVIES_FILE)
    if rating is not None:
        filtered_movies = []
        for movie in all_movies:
            if movie["rating"] >= rating:
                filtered_movies.append(movie)
        all_movies = filtered_movies
    return all_movies




