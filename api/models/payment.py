from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Boolean
from sqlalchemy.orm import relationship
from datetime import date
from ..dependencies.database import Base

class Payment(Base):
    __tablename__ = "payment"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    card_num = Column(Integer, unique=False, nullable=True, server_default='0')
    expiration_date = Column(DATETIME, nullable=True, server_default=str(date.today()))
    complete = Column(Boolean)
    
