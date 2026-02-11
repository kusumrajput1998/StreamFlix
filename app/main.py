from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.database import engine, Base
from app.routes import movies
import app.models   # 👈 IMPORTANT (registers models)
from app.routes import auth


app = FastAPI(title="StreamFlix API")

Base.metadata.create_all(bind=engine)
app.include_router(auth.router)

app.include_router(movies.router)

app.mount("/", StaticFiles(directory="static", html=True), name="static")

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/hello")
def hello():
    return {"message": "New deployment working!"}

