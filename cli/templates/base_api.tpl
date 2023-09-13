from fastapi import FastAPI, HTTPException
from database import engine, db_dependency
import models
import dto


app = FastAPI()

models.Base.metadata.create_all(bind=engine)
