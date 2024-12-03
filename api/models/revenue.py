from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Revenue(Base):
    __tablename__ = "revenue"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    revenue_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    total_revenue = Column(DECIMAL(6,2), nullable=False, server_default='0.0')
    
    order_id = Column(Integer, ForeignKey("orders.id"))
