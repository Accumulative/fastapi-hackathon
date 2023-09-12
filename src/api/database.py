from contextlib import asynccontextmanager
from typing import Annotated

import asyncpg
from pydantic import BaseModel, create_model
from sqlalchemy import TIMESTAMP, MetaData
from sqlalchemy.dialects.postgresql.asyncpg import (
    AsyncAdapt_asyncpg_connection,
    AsyncAdapt_asyncpg_dbapi,
)
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy.sql import func
from sqlalchemy.util import await_only

from src.api.config import DATABASE

dbapi = AsyncAdapt_asyncpg_dbapi(asyncpg)


def connect_with_connector():
    """
    Initializes a connection pool for a Cloud SQL instance of Postgres.

    Uses the Cloud SQL Python Connector package.
    """
    # Note: Saving credentials in environment variables is convenient, but not
    # secure - consider a more secure solution such as
    # Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
    # keep secrets safe.

    db_user = DATABASE.USER
    db_pass = DATABASE.PASSWORD
    db_name = DATABASE.NAME

    async def getconn() -> asyncpg.Connection:
        conn: asyncpg.Connection = await asyncpg.connect(
            user=db_user,
            password=db_pass,
            host=DATABASE.HOST,
            database=db_name,
        )
        return conn

    def getconn_sync() -> AsyncAdapt_asyncpg_connection:
        return AsyncAdapt_asyncpg_connection(
            dbapi,
            await_only(getconn()),
        )

    # The Cloud SQL Python Connector can be used with SQLAlchemy
    # using the 'creator' argument to 'create_engine'
    pool = create_async_engine(
        "postgresql+asyncpg://",
        creator=getconn_sync,
        echo=False,
        # ...
    )
    return pool


engine = connect_with_connector()

SessionLocal = async_sessionmaker(
    autocommit=False, autoflush=False, bind=engine, expire_on_commit=False
)

metadata_obj = MetaData()


class Base(DeclarativeBase, AsyncAttrs):
    created_at = mapped_column(TIMESTAMP, server_default=func.now())
    updated_at = mapped_column(
        TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp()
    )


# Dependency
async def get_database():
    async with SessionLocal() as session:
        yield session


# Async context manager
@asynccontextmanager
async def use_database():
    try:
        session = SessionLocal()
        yield session
    finally:
        await session.close()


S_VARCHAR = 20
M_VARCHAR = 255
L_VARCHAR = 2048
XL_VARCHAR = 2048

str_xl = Annotated[str, XL_VARCHAR]
str_l = Annotated[str, L_VARCHAR]
str_m = Annotated[str, M_VARCHAR]
str_s = Annotated[str, S_VARCHAR]

intpk = Annotated[int, mapped_column(primary_key=True)]


def is_pydantic_model(obj):
    try:
        return issubclass(obj, BaseModel)
    except TypeError:
        return False


def partial(Model: BaseModel, name: str | None = None) -> type[BaseModel]:
    fields = {}
    for k, v in Model.model_fields.items():
        if is_pydantic_model(v.annotation):
            fields[k] = (partial(v.annotation), None)
        else:
            fields[k] = (v.annotation, None)
    return create_model(name if name is not None else Model.__name__, **fields)
