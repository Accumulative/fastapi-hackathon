from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi


links = """
---
## Documentation Links

These links connect to the documentation for the sub-applications.

<details>
<summary>**Redoc V1**</summary>

* **[Sandbox](/v1/sandbox/redoc)**
</details>

<details>
<summary>**Swagger V1**</summary>

* **[Sandbox](/v1/sandbox/docs)**
</details>
---
"""


def docs_generator(app: FastAPI, title: str, description: str, prefix: str = "/"):
    def openapi_schema_generator():
        if app.openapi_schema:
            return app.openapi_schema
        
        openapi_schema = get_openapi(
            title=f"Bolt - {title}",
            version="0.1",
            description=links + description,
            routes=app.routes,
            terms_of_service="https://bolt.dev/terms",
            contact={
                "name": "bolt support",
                "url": "https://bolt.dev",
                "email": "support@bolt.dev",
            },
        )

        openapi_schema["paths"] = {prefix + key: value for key, value in openapi_schema["paths"].items()}

        app.openapi_schema = openapi_schema

        return app.openapi_schema

    return openapi_schema_generator
