from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ReviewBase(BaseModel):
    content: str
    stars: int
    order_id: int


class ReviewCreate(ReviewBase):
    pass


class ReviewUpdate(BaseModel):
    content: Optional[str] = None
    stars: Optional[int] = None
    order_id: Optional[int] = None


class Review(ReviewBase):
    id: int

    class ConfigDict:
        from_attributes = True
