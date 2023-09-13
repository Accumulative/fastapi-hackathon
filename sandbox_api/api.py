from fastapi import FastAPI, HTTPException, status
from openapi import docs_generator
from database import db_dependency
from .models import SandboxORM
from .dto import SandboxDTO


app = FastAPI(openapi_prefix="")
app.openapi = docs_generator(
    app, "Sandbox", "Sandbox API helps do...", "/v1/sandbox"
)


@app.get("/sandboxs", tags=["sandbox"])
def get_sandbox(db: db_dependency):
    return db.query(SandboxORM).all()


@app.post("/sandboxs", tags=["sandbox"], status_code=status.HTTP_201_CREATED)
def create_sandbox(sandbox: SandboxDTO, db: db_dependency):
    new_item = SandboxORM(**sandbox.model_dump())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


@app.get("/sandboxs/{sandbox_id}", tags=["sandbox"])
def get_sandbox_by_id(sandbox_id: int, db: db_dependency):
    item = db.query(SandboxORM).filter(SandboxORM.id == sandbox_id).first()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Record with id={sandbox_id} not found")
    return item


@app.put("/sandboxs/{sandbox_id}", tags=["sandbox"])
def update_sandbox(sandbox_id: int, sandbox: SandboxDTO, db: db_dependency):
    item = db.query(SandboxORM).filter(SandboxORM.id == sandbox_id).first()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Record with id={sandbox_id} not found")
    item.name = sandbox.name
    db.commit()
    db.refresh(item)
    return item

