from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class RevenueBase(BaseModel):
    total: float

class RevenueCreate(RevenueBase):
    pass

class RevenueUpdate(RevenueBase):
    total: Optional[float] = None

class Revenue(RevenueBase):
    id: int

    class ConfigDict:
        from_attributes = True