from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class RevenueBase(BaseModel):
    total_revenue: float

class RevenueCreate(RevenueBase):
    pass

class RevenueUpdate(RevenueBase):
    total_revenue: Optional[float] = None
    date: Optional[datetime] = None

class Revenue(RevenueBase):
    id: int
    revenue_date: Optional[datetime] = None

    class ConfigDict:
        from_attributes = True