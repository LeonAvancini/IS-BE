from fastapi import FastAPI
from app.routers import cards
from fastapi_sqlalchemy import DBSessionMiddleware
from app.config.settings import settings

app = FastAPI()
app.add_middleware(DBSessionMiddleware, db_url=settings.SQLALCHEMY_DATABASE_URL)


@app.get("/")
def read_root():
    return {"Hello": "World"}


app.include_router(cards.router)
