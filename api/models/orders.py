from sqlalchemy import Column, Boolean,ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(String(100))
    order_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    description = Column(String(300))
    takeout = Column(Boolean)

    order_details = relationship("OrderDetail", back_populates="order")
    reviews = relationship("Review", back_populates="order")
    complete_orders = relationship("complete_orders", back_populates="order")
    user = relationship("user", back_populates="orders")
    