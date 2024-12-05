from datetime import date
from pydantic import BaseModel
from typing import Optional

class PaymentBase(BaseModel):
    card_num: str = "1234-567-8910"
    expiration_date: date
    complete: bool = False

class PaymentCreate(PaymentBase):
    pass

class PaymentUpdate(PaymentBase):
    card_num: Optional[str] = None
    expiration_date: Optional[date] = None
    complete: Optional[bool] = None

class Payment(PaymentBase):
    id: int

    class ConfigDict:
        from_attributes = True