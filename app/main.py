from fastapi import FastAPI

from app.core.config import settings
from app.core.logger import setup_logger
from app.db.base import Base
from app.db.session import engine
from app.routes.address import router

setup_logger()

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Address Book API")

app.include_router(router, prefix=settings.API_VERSION)
