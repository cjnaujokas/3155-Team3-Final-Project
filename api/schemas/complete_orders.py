from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class complete_ordersBase(BaseModel):
    order_id: int


class complete_ordersCreate(complete_ordersBase):
    pass


class complete_ordersUpdate(BaseModel):
    order_id: Optional[str] = None


class complete_ordersResource(complete_ordersBase):
    id: int

    class ConfigDict:
        from_attributes = True
