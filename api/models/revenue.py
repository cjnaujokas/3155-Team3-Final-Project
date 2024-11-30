from sqlalchemy import Column, Integer, DateTime, DECIMAL
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Revenue(Base):
    __tablename__ = "revenue"

    # Columns
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    revenue_date = Column(DateTime, nullable=False, default=datetime.utcnow)  # Date of revenue
    total_revenue = Column(DECIMAL(10, 2), nullable=False, default=0.00)  # Total revenue

    # Relationships (assuming it relates to orders or other models)
    orders = relationship("Order", back_populates="revenue")  # Fix the model reference

    def __repr__(self):
        return f"<Revenue(id={self.id}, revenue_date={self.revenue_date}, total_revenue={self.total_revenue})>"

    def to_dict(self):
        return {
            "id": self.id,
            "revenue_date": self.revenue_date.isoformat(),
            "total_revenue": float(self.total_revenue),  # Convert Decimal to float for JSON compatibility
        }

    # Business Logic Methods
    @classmethod
    def calculate_daily_revenue(cls, session, date: datetime):
        """
        Calculate total revenue for a specific date.
        TODO: Implement aggregation logic to calculate daily revenue.
        """
        pass

    @classmethod
    def calculate_monthly_revenue(cls, session, month: int, year: int):
        """
        Calculate total revenue for a specific month.
        TODO: Implement logic to filter and sum revenue for the given month and year.
        """
        pass