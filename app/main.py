from app.models import Movie
from app.database import SessionLocal

@app.on_event("startup")
def seed_data():
    db = SessionLocal()
    if db.query(Movie).count() == 0:
        db.add_all([
            Movie(title="Inception", description="Sci-fi thriller", banner_url=""),
            Movie(title="Interstellar", description="Space drama", banner_url=""),
            Movie(title="The Dark Knight", description="Batman movie", banner_url=""),
        ])
        db.commit()
    db.close()

