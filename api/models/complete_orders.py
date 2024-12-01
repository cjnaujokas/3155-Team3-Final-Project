from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class CompleteOrders(Base):
    __tablename__ = "complete_orders"
    #columns  
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)  
    completion_status = Column(String(100), nullable=False)

<<<<<<< Updated upstream
    #relationships
    order = relationship("Order", back_populates="complete_orders") #link to orders
=======
    # Relationships
    order = relationship("Order", back_populates="complete_orders")
>>>>>>> Stashed changes
