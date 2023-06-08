from pydantic import BaseSettings


class Settings(BaseSettings):
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'
    title: str = 'Благотворительного фонда поддержки котиков QRKot'
    secret: str = 'SECRET'

    class Config:
        env_file = '.env'


settings = Settings()


MIN_LENGTH = 1  # Минимальная длинна для строки
MAX_LENGTH = 100  # Максимальная длинна для строки
EXAMPLE_AMOUNT = 2000  # пример для суммы инвестирования
REG_NAME = r'^[А-Яа-яA-Za-z0-9\s]+$'  # Выражение для проверки name
DEFAULT_INVESTED = 0  # значение по-умолчанию для инвестиций
