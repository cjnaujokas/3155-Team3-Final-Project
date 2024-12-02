from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from ..dependencies.database import Base

class Promo_Codes(Base):
    __tablename__ = "promotions"

    # Columns
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    code = Column(String(50), unique=True, nullable=False)  
    discount_percentage = Column(Float, nullable=False)  # Discount percentage (newly added)
    expiration = Column(DateTime, nullable=False, default=datetime.utcnow)  
    description = Column(String(300), nullable=True)  
