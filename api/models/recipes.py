from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Recipe(Base):
    __tablename__ = "recipes"

    # Columns
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    food_item_id = Column(Integer, ForeignKey("food_items.id"), nullable=False)
    resource_id = Column(Integer, ForeignKey("resources.id"), nullable=False)
    amount = Column(Integer, index=True, nullable=False, default=0)

    # Relationships
    food_item = relationship("FoodItem", back_populates="recipes")
    resource = relationship("Resource", back_populates="recipes")
    reviews = relationship("Review", back_populates="recipe")
