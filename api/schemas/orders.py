from datetime import date
from typing import Optional
from pydantic import BaseModel
from .order_details import OrderDetail
from .reviews import Review
from .complete_orders import complete_ordersResource



class OrderBase(BaseModel):
    customer_name: str
    description: Optional[str] = None
    takeout: Optional[bool] = False


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    customer_name: Optional[str] = None
    description: Optional[str] = None
    takeout: Optional[bool]


class Order(OrderBase):
    id: int
    order_date: Optional[date] = None
    order_details: list[OrderDetail] = None
    reviews: list[Review] = None
    tracking_number: Optional[int] = None
    

    class ConfigDict:
        from_attributes = True
