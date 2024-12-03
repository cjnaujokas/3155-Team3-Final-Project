from datetime import date
from pydantic import BaseModel
from typing import Optional

class PromoBase(BaseModel):
    code: int
    expiration: date
    description: Optional[str] = None

class PromoCreate(PromoBase):
    pass

class PromoUpdate(BaseModel):
    code: Optional[int] = None
    expiration: Optional[date] = None
    description: Optional[str] = None

class Promo(PromoBase):
    id: int

    class ConfigDict:
        from_attributes = True