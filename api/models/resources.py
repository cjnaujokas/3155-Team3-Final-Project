from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class Resource(Base):
    __tablename__ = "resources"

    # Columns
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    item = Column(String(100), unique=True, nullable=False)  # Name of the resource/ingredient
    amount = Column(Integer, index=True, nullable=False, default=0)  # Quantity of the resource in stock

    # Relationships
    recipes = relationship("Recipe", back_populates="resource")  # Back-populates the Recipe relationship

    def __repr__(self):
        return f"<Resource(id={self.id}, item={self.item}, amount={self.amount})>"

    def to_dict(self):
        return {
            "id": self.id,
            "item": self.item,
            "amount": self.amount,
        }

    # Business Logic Methods
    def checking_ingredient_stock(self):
        """
        Check the stock level of the resource.
        TODO: Implement logic to return the current stock level.
        """
        pass

    def low_stock_alert(self, threshold: int):
        """
        Alert if the stock level falls below a threshold.
        TODO: Implement logic to check if the stock is below the given threshold.
        """
        pass

    def update_stock(self, amount: int):
        """
        Update the stock of the resource.
        TODO: Implement logic to increase or decrease the stock by a specified amount.
        """
        pass
