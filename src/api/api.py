from fastapi import FastAPI
from fastapi.logger import logger
from fastapi.middleware.cors import CORSMiddleware
from src.api.config import GENERAL
import logging

# routers
from src.api.routers.user import v1_router as v1_user_router
from src.api.routers.user import v2_router as v2_user_router

app = FastAPI()

# Logging configuration

if GENERAL.ENV == "local":
    logger.setLevel(logging.DEBUG)

# Uncomment for automatic migrations
# from src.api.common.database import Base, engine
# Base.metadata.create_all(bind=engine)

origins_regex = r"https://.*\.your-site\.jp"

if GENERAL.ENV in ["local", "dev"]:
    origins_regex = r".*"

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origin_regex=origins_regex,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["content-disposition"],
    max_age=3600,
)

app.include_router(v1_user_router, prefix="/api")
app.include_router(v2_user_router, prefix="/api")
