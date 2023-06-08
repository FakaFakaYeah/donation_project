from fastapi import FastAPI

from app.api import main_router
from app.core.config import settings

app = FastAPI(title=settings.title)
app.include_router(main_router)
