from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base
#OrderDetail Table
class OrderDetail(Base):
    __tablename__ = "order_details"
    #columns
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    food_item_id = Column(Integer, ForeignKey("food_items.id"))
    amount = Column(Integer, index=True, nullable=False)
    
    #relationships
    food_item = relationship("FoodItem", back_populates="order_details")
    order = relationship("Order", back_populates="order_details")
