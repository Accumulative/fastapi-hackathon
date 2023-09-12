from fastapi import APIRouter, Depends
from src.api.database import get_database
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.api.dto.user import UserDTO
from src.api.models.user import UserORM

# vanilla implementation
v1_router = APIRouter(prefix="/v1/users", tags=["v1"])
@v1_router.get("/", response_model=list[UserDTO])
async def list_users(session: AsyncSession = Depends(get_database)):
    users = await session.scalars(select(UserORM))
    return users


# class implementation
class UserRouter(APIRouter):
    def __init__(self, **kwargs):
        super().__init__(
            prefix="/v2/users",
            tags=["v2"],
            **kwargs,
        )

        self.add_api_route(
            path="/",
            endpoint=self.list_users,
            methods=["GET"],
            response_model=list[UserDTO],
        )

    async def list_users(self, session: AsyncSession = Depends(get_database)):
        return await session.scalars(select(UserORM))

v2_router = UserRouter()