from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String(300), nullable=False)
    stars = Column(Integer, nullable=False, server_default='0')
    recipe_id = Column(Integer, ForeignKey("recipes.id"), nullable=False)  # Foreign key linking to Recipe

    # Relationships
    recipe = relationship("Recipe", back_populates="reviews")
