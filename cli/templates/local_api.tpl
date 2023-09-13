from fastapi import FastAPI, HTTPException, status
from database import db_dependency
from .models import ${name_title}ORM
from .dto import ${name_title}DTO


app = FastAPI()


@app.get("/${name}", tags=["${name}"])
def get_${name}(db: db_dependency):
    return db.query(${name_title}ORM).all()


@app.post("/${name}", tags=["${name}"], status_code=status.HTTP_201_CREATED)
def create_${name}(${name}: ${name_title}DTO, db: db_dependency):
    new_item = ${name_title}ORM(**${name}.model_dump())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


@app.get("/${name}/{${name}_id}", tags=["${name}"])
def get_${name}_by_id(${name}_id: int, db: db_dependency):
    item = db.query(${name_title}ORM).filter(${name_title}ORM.id == ${name}_id).first()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Record with id={${name}_id} not found")
    return item


@app.put("/${name}/{${name}_id}", tags=["${name}"])
def update_${name}(${name}_id: int, ${name}: ${name_title}DTO, db: db_dependency):
    item = db.query(${name_title}ORM).filter(${name_title}ORM.id == ${name}_id).first()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Record with id={${name}_id} not found")
    item.name = ${name}.name
    db.commit()
    db.refresh(item)
    return item

