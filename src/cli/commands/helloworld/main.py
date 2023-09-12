from src.api.database import use_database
from src.api.models.user import Locale, Role, UserORM

from src.cli.commands.base import AsyncTyper

app = AsyncTyper()


@app.async_command()
async def command(username: str, email: str, role: Role):
    async with use_database() as session:
        user = UserORM(username=username, email=email, role=role, locale=Locale.Japanese)
        session.add(user)
        await session.commit()
        await session.refresh(user)
        print(user)

