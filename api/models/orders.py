from sqlalchemy import Column, Boolean, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from datetime import datetime
from ..dependencies.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(String(100))
    order_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    description = Column(String(300), nullable=True)
    takeout = Column(Boolean, nullable=False, default=False)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)  # Foreign key linking to User

    # Relationships
    user = relationship("User", back_populates="orders")
    order_details = relationship("OrderDetail", back_populates="order", cascade="all, delete-orphan")
    complete_orders = relationship("CompleteOrders", back_populates="order", cascade="all, delete-orphan")
    revenue = relationship("Revenue", back_populates="order", uselist=False)
