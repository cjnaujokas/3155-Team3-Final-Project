from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class usersBase(BaseModel):
    username: str
    password: str
    order_id: Optional[int] = None


class usersCreate(usersBase):
    pass


class usersUpdate(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None
    order_id: Optional[int] = None



class usersResource(usersBase):
    id: int

    class ConfigDict:
        from_attributes = True
