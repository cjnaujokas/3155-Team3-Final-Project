from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class user(Base):
    __tablename__ = "users"

    #columns
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), unique=True, nullable=False)
    order_id = Column(Integer, ForeignKey("orders.id"))

    #relationships
    orders = relationship("Order", back_populates="user")
