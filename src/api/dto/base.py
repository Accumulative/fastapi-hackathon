from datetime import datetime

from pydantic import BaseModel


class BaseORMDTO(BaseModel):
    created_at: datetime
    updated_at: datetime
