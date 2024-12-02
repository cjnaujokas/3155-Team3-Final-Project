from sqlalchemy import Column, Integer, DateTime, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Revenue(Base):
    __tablename__ = "revenue"

    # Columns
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    revenue_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    total_revenue = Column(DECIMAL(6, 2), nullable=False, server_default='0.0')

    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)  # Foreign key linking to Order

    # Relationships
    order = relationship("Order", back_populates="revenue")
