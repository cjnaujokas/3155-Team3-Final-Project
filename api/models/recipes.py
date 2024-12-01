<<<<<<< Updated upstream
from sqlalchemy import Column, ForeignKey, Integer, Float
=======
from sqlalchemy import Column, ForeignKey, Integer
>>>>>>> Stashed changes
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Recipe(Base):
    __tablename__ = "recipes"

    # Columns
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
<<<<<<< Updated upstream
    food_item_id = Column(Integer, ForeignKey("food_items.id"), nullable=False)  # Foreign key to FoodItem
    resource_id = Column(Integer, ForeignKey("resources.id"), nullable=False)  # Foreign key to Resource
    amount = Column(Float, nullable=False, default=0.0)  # Amount of the resource used

    # Relationships
    food_item = relationship("FoodItem", back_populates="recipes")  # Back-populates FoodItem relationship
    resource = relationship("Resource", back_populates="recipes")  # Back-populates Resource relationship

    def __repr__(self):
        return (
            f"<Recipe(id={self.id}, food_item_id={self.food_item_id}, "
            f"resource_id={self.resource_id}, amount={self.amount})>"
        )

    def to_dict(self):
        return {
            "id": self.id,
            "food_item_id": self.food_item_id,
            "resource_id": self.resource_id,
            "amount": self.amount,
        }

    # CRUD Operations
    @classmethod
    def create_recipe(cls, session, **kwargs):
        """
        Create a new recipe.
        TODO: Implement logic to create a recipe.
        """
        pass

    @classmethod
    def get_recipe(cls, session, recipe_id: int):
        """
        Retrieve a recipe by ID.
        TODO: Implement logic to retrieve a specific recipe.
        """
        pass

    @classmethod
    def update_recipe(cls, session, recipe_id: int, **kwargs):
        """
        Update an existing recipe.
        TODO: Implement logic to update a recipe.
        """
        pass

    @classmethod
    def delete_recipe(cls, session, recipe_id: int):
        """
        Delete a recipe.
        TODO: Implement logic to delete a recipe by its ID.
        """
        pass

    @classmethod
    def list_all_recipes(cls, session):
        """
        List all recipes.
        TODO: Implement logic to list all recipes.
        """
        pass
=======
    food_item_id = Column(Integer, ForeignKey("food_items.id"), nullable=False)
    resource_id = Column(Integer, ForeignKey("resources.id"), nullable=False)
    amount = Column(Integer, index=True, nullable=False, default=0)

    # Relationships
    food_item = relationship("FoodItem", back_populates="recipes")
    resource = relationship("Resource", back_populates="recipes")
    reviews = relationship("Review", back_populates="recipe")
>>>>>>> Stashed changes
