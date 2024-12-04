from sqlalchemy import Column, Boolean,ForeignKey, Integer, String, DECIMAL, DATETIME, DATE, text
from sqlalchemy.orm import relationship
from datetime import date
from ..dependencies.database import Base
import random


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(String(100))
    order_date = Column(DATE, nullable=False, server_default=str(date.today()))
    description = Column(String(300))
    takeout = Column(Boolean)
    tracking_number = Column(Integer, unique=True, nullable=True, default=lambda: random.randint(100000, 999999))

    order_details = relationship("OrderDetail", back_populates="order")
    reviews = relationship("Review", back_populates="order")
    complete_orders = relationship("complete_orders", back_populates="order")
    user = relationship("user", back_populates="orders")
    