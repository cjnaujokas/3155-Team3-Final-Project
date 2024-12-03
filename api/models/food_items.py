from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

#FoodItem Table
class FoodItem(Base):
    __tablename__ = "food_items"

    #columns
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    food_item_name = Column(String(100), unique=True, nullable=True)
    price = Column(DECIMAL(4, 2), nullable=False, server_default='0.0')
    
    #relationships
    recipes = relationship("Recipe", back_populates="food_item")
    order_details = relationship("OrderDetail", back_populates="food_item")
