from sqlalchemy import Column, ForeignKey, Integer, DECIMAL
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class OrderDetail(Base):
    __tablename__ = "order_details"
    #Columns
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)  # Foreign key linking to Order
    food_item_id = Column(Integer, ForeignKey("food_items.id"), nullable=False)  # Foreign key linking to FoodItem
    amount = Column(Integer, index=True, nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)  # Price of the item (NEW ADDITION TO TABLE)

    # Relationships
    food_item = relationship("FoodItem", back_populates="order_details")  # Matches the corrected class name
    order = relationship("Order", back_populates="order_details")
