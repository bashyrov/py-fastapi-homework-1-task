from pydantic import BaseModel
import datetime


class MovieDetailResponseSchema(BaseModel):
    id: int
    name: int
    date: datetime.date
    score: float
    genre: str
    overview: str
    crew: str
    orig_title: str
    status: str
    orig_lang: str
    budget: float
    revenue: float
    country: str


    class Config:
        orm_mode = True


class MovieListResponseSchema(BaseModel):
    prev_page: int | None
    next_page: int | None
    total_pages: int
    total_items: int