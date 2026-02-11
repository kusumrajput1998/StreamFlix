from pydantic import BaseModel

class MovieBase(BaseModel):
    title: str
    description: str
    video_url: str

class MovieCreate(MovieBase):
    pass

class MovieResponse(MovieBase):
    id: int

    class Config:
        from_attributes = True
