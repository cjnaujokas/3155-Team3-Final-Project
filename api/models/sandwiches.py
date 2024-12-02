from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class MenuItem(Base):
    __tablename__ = "menu_items"

    # Columns
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    item_name = Column(String(100), unique=True, nullable=False)  # Name of the menu item
    price = Column(Float, nullable=False, default=0.0)  # Price of the menu item

    # Relationships
    recipes = relationship("Recipe", back_populates="menu_item")  # Link to Recipe model
    order_details = relationship("OrderDetail", back_populates="menu_item")  # Link to OrderDetail model
