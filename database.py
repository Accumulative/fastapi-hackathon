from fastapi import Depends
from typing import Annotated
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from config import DATABASE_URI

engine = create_engine(DATABASE_URI)

AsyncSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = scoped_session(AsyncSession)
    
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
