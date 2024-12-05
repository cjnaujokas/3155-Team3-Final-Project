from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Boolean
from sqlalchemy.orm import relationship
from datetime import date
from ..dependencies.database import Base

class Payment(Base):
    __tablename__ = "payment"
    #columns
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    card_num = Column(String(15), nullable=False)
    expiration_date = Column(DATETIME, nullable=True, server_default=str(date.today()))
    complete = Column(Boolean)
    
