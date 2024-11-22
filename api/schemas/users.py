from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class usersBase(BaseModel):
    password: str
    order_id: int


class usersCreate(usersBase):
    pass


class usersUpdate(BaseModel):
    password: Optional[str] = None
    order_id: Optional[int] = None



class usersResource(usersBase):
    user_id: int

    class ConfigDict:
        from_attributes = True
