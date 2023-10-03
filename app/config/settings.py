from pydantic import BaseConfig


class Settings(BaseConfig):
    SQLALCHEMY_DATABASE_URL = "postgresql://postgres:admin@localhost/postgres"


settings = Settings()
