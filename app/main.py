from fastapi import FastAPI

from app.core.config import settings
from app.api.routers import main_router

app = FastAPI(title=settings.title, description=settings.description)
app.include_router(main_router)