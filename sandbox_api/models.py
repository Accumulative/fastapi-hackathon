from typing import Annotated
from sqlalchemy.orm import Mapped, mapped_column, relationship
from settings import Base


intpk = Annotated[int, mapped_column(primary_key=True)]


class SandboxORM(Base):
    __tablename__ = "sandbox"

    id: Mapped[intpk]
