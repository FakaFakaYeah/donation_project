from pydantic import BaseSettings


class Settings(BaseSettings):
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'
    title: str
    description: str
    secret: str = 'SECRET'

    class Config:
        env_file = '.env'


settings = Settings()