from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.database import engine, Base
from app.routes import movies

app = FastAPI(title="StreamFlix API")

# Commented because DB not running yet
Base.metadata.create_all(bind=engine)

app.include_router(movies.router)

app.mount("/", StaticFiles(directory="static", html=True), name="static")

@app.get("/health")
def health():
    return {"status": "healthy"}
