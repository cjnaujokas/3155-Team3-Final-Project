from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Review(Base):
    __tablename__ = "reviews"

    #columns
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    content = Column(String(100), unique=True, nullable=False)
    stars = Column(Integer, index=True, nullable=False, server_default='0.0')
    order_id = Column(Integer, ForeignKey("orders.id"))

    #relationships
    order = relationship("Order", back_populates="reviews")