import os

# TODO: use pydantic-settings


class DATABASE:
    USER = os.getenv("DATABASE_USER", "user")
    PASSWORD = os.getenv("DATABASE_PASSWORD", "password")
    HOST = os.getenv("DATABASE_HOST", "db")
    NAME = os.getenv("DATABASE_NAME", "hello-world")

    TEST_USER = os.getenv("DATABASE_USER", "user")
    TEST_PASSWORD = os.getenv("DATABASE_PASSWORD", "password")
    TEST_HOST = os.getenv("DATABASE_HOST", "localhost")
    TEST_NAME = os.getenv("DATABASE_NAME", "test")


class GENERAL:
    ENV = os.getenv("ENV", "local")
