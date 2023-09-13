from typing import Annotated
from sqlalchemy.orm import Mapped, mapped_column, relationship
from settings import Base


intpk = Annotated[int, mapped_column(primary_key=True)]


class ${name_title}ORM(Base):
    __tablename__ = "${name}"

    id: Mapped[intpk]
