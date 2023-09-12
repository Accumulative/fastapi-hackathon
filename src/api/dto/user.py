from pydantic import BaseModel, EmailStr, Field
from src.api.database import M_VARCHAR
from src.api.dto.base import BaseORMDTO
from src.api.models.user import Locale, Role


class UserCreate(BaseModel):
    locale: str = Field(
        title="Locale",
        description="The locale for this user",
        examples=[Locale.Japanese],
        default=Locale.Japanese,
    )
    email: EmailStr = Field(
        title="Email",
        description="The user's email address",
        examples=["test@example.com"],
    )
    username: str = Field(
        title="Username",
        description="The user's username",
        examples=["test user"],
        max_length=M_VARCHAR,
    )
    role: Role = Field(
        title="Role",
        description="The role this user performs within the system. It controls their access to functionality.",
        default=Role.Admin,
    )


class UserDTO(UserCreate, BaseORMDTO):
    id: int = Field(title="User ID", description="The internal ID for this user.")

    model_config = {
        "from_attributes": True,
    }
