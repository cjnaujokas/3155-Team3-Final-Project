from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class PromoBase(BaseModel):
    promocode: int
    description: Optional[str] = None

class PromoCreate(PromoBase):
    pass

class PromoUpdate(BaseModel):
    promocode: Optional[int] = None
    description: Optional[str] = None

class Promo(PromoBase):
    id: int

    class ConfigDict:
        from_attributes = True