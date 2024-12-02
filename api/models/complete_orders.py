from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class complete_orders(Base):
    __tablename__ = "complete_orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"))

    # complete_orders = relationship("OrderDetail", back_populates="order")
    order = relationship("Order", back_populates="complete_orders")