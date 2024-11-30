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

    def __repr__(self):
        return (
            f"<MenuItem(id={self.id}, item_name={self.item_name}, price={self.price})>"
        )

    def to_dict(self):
        """Convert the object to a dictionary for easier serialization."""
        return {
            "id": self.id,
            "item_name": self.item_name,
            "price": self.price,
        }

    # CRUD Operations
    @classmethod
    def create_menu_item(cls, session, item_name: str, price: float):
        """
        Create a new menu item.
        TODO: Implement logic to create a menu item.
        """
        pass

    @classmethod
    def update_menu_item(cls, session, menu_item_id: int, **kwargs):
        """
        Update an existing menu item.
        TODO: Implement logic to update a menu item by its ID.
        """
        pass

    @classmethod
    def delete_menu_item(cls, session, menu_item_id: int):
        """
        Delete a menu item.
        TODO: Implement logic to delete a menu item by its ID.
        """
        pass

    @classmethod
    def get_all_menu_items(cls, session):
        """
        Retrieve all menu items.
        TODO: Implement logic to retrieve all menu items.
        """
        pass

    @classmethod
    def get_menu_item_by_id(cls, session, menu_item_id: int):
        """
        Retrieve a specific menu item by ID.
        TODO: Implement logic to retrieve a menu item by its ID.
        """
        pass
