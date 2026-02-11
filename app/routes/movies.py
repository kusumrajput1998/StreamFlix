from fastapi import APIRouter

router = APIRouter()

@router.get("/movies")
def get_movies():
    return [
        {"title": "Inception"},
        {"title": "Interstellar"},
        {"title": "The Dark Knight"},
        {"title": "Avengers"}
    ]


