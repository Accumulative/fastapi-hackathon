from enum import Enum

from sqlalchemy.orm import Mapped, mapped_column

from src.api.database import Base, intpk, str_m, str_s


class Locale(str, Enum):
    English = "En"
    Japanese = "Ja"


class Role(str, Enum):
    User = "User"
    Admin = "Admin"
    RootAdmin = "Root Admin"


class AccountStatus(str, Enum):
    Active = "Active"
    Suspended = "Suspended"


class UserORM(Base):
    __tablename__ = "users"

    id: Mapped[intpk]
    locale: Mapped[str_s]
    status: Mapped[str_s] = mapped_column(default=AccountStatus.Active)
    username: Mapped[str_m]
    email: Mapped[str_m]
    role: Mapped[str_s]

    def __repr__(self) -> str:
        return f"id: {self.id} || email: {self.email}"

    @property
    def is_active(self):
        return self.status == AccountStatus.Active
