from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class user(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    password = Column(String(100), unique=True, nullable=False)
    order_id = Column(Integer, nullable=False, autoincrement=True)

    orders = relationship("Order", back_populates="user")
