from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIRoute
from database import Base, engine
from openapi import docs_generator
import re

# import apps here
from sandbox_api.api import app as sandbox_app

# MAIN

app = FastAPI(openapi_prefix="")

app.openapi = docs_generator(
    app,
    "API",
    "FastAPI Project created using Bolt! ⚡️",
    "/"
)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["content-disposition"],
    max_age=3600,
)

# DATABASE

Base.metadata.create_all(bind=engine)

# APPS

v1_app = APIRouter()

app.mount("/v1", v1_app)

APPS = {
    "sandbox": sandbox_app,
}


def generate_path(route: APIRoute, prefix: str) -> str:
    operation_id = route.path_format
    operation_id = re.sub(r"\W", "_", operation_id)
    # check if the route has methods
    assert route.methods
    operation_id = "_".join([list(route.methods)[0].lower(), operation_id])
    return operation_id


for prefix, sub_app in APPS.items():
    v1_app.mount(f"/{prefix}", sub_app)

    for route in sub_app.routes:
        if isinstance(route, APIRoute):
            route.operation_id = generate_path(route, prefix)
