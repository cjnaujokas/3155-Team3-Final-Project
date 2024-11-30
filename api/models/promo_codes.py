from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from ..dependencies.database import Base

class Promo_Codes(Base):
    __tablename__ = "promotions"

    # Columns
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    code = Column(String(50), unique=True, nullable=False)  
    discount_percentage = Column(Float, nullable=False)  # Discount percentage (newly added)
    expiration = Column(DateTime, nullable=False, default=datetime.utcnow)  
    description = Column(String(300), nullable=True)  

    def __repr__(self):
        return (
            f"<Promo_Codes(id={self.id}, code={self.code}, "
            f"discount_percentage={self.discount_percentage}, expiration={self.expiration})>"
        )

    def to_dict(self):
        return {
            "id": self.id,
            "code": self.code,
            "discount_percentage": self.discount_percentage,
            "expiration": self.expiration.isoformat(),
            "description": self.description,
        }

    # CRUD Operations
    @classmethod
    def create_promo(cls, session, **kwargs):
        """
        Create a new promo code.
        TODO: Implement logic for adding a promo code.
        """
        pass

    @classmethod
    def apply_promo_code(cls, session, code: str):
        """
        Apply a promo code.
        TODO: Implement validation and application of promo codes.
        """
        pass

    @classmethod
    def validate_promo_code(cls, session, code: str):
        """
        Validate a promo code.
        TODO: Check if the promo code exists and is not expired.
        """
        pass

    @classmethod
    def delete_promo_code(cls, session, promo_id: int):
        """
        Delete a promo code.
        TODO: Implement deletion of a promo code by its ID.
        """
        pass

    @classmethod
    def list_all_promo_codes(cls, session):
        """
        List all promo codes.
        TODO: Retrieve and return all promo codes.
        """
        pass
