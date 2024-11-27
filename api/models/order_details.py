from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from datetime import datetime
from ..dependencies.database import Base

class OrderDetail(Base):
    __tablename__ = "order_details"
    #Columns
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    food_item_id = Column(Integer, ForeignKey("food_items.id"))
    amount = Column(Integer, index=True, nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)  # Price of the item (NEW ADDITION TO TABLE)

    #Relationships
    food_item = relationship("FoodItem", back_populates="order_details")
    order = relationship("Order", back_populates="order_details")

    def __repr__(self):
        return (
            f"<OrderDetail(id={self.id}, order_id={self.order_id}, "
            f"food_item_id={self.food_item_id}, amount={self.amount}, price={self.price})>"
        )
    def to_dict(self):
        """Convert the object to a dictionary for easier serialization."""
        return {
            "id": self.id,
            "order_id": self.order_id,
            "food_item_id": self.food_item_id,
            "amount": self.amount,
            "price": float(self.price),  # Convert Decimal to float
        }
    
    #CRUD
    @classmethod
    def create_order_detail(cls, session: Session, order_id: int, food_item_id: int, amount: int, price: float):
        #create new order detail
        try:
            new_details = cls(order_id=order_id, food_item_id=food_item_id, amount=amount, price=price)
            session.add(new_details)
            session.commit()
            return new_details
        except Exception as e:
            session.rollback()
            raise e
        
    @classmethod
    def get_order_details(cls, session: Session, order_id: int):
        #get order details
        return session.query(cls).filter(cls.order_id == order_id).first()
    
    @classmethod
    def update_order_detail(cls, session: Session, detail_id: int, **kwargs):
        #update order detail
        detail = session.query(cls).filter(cls.id == detail_id).first()
        if detail:
            for key, value in kwargs.items():
                setattr(detail, key, value)
            session.commit()
            return detail
        else:
            return None
        
    @classmethod
    def delete_order_detail(cls, session: Session, detail_id: int):
        #delete order details
        try:
            detail = session.query(cls).filter(cls.id == detail_id).first()
            if detail:
                session.delete(detail)
                session.commit()
            else:
                raise ValueError("Order detail not found.")
        except Exception as e:
            session.rollback()
            raise e

    @classmethod
    def get_all_details_for_order(cls, session: Session, order_id: int):
        #get all details for an order
        return session.query(cls).filter_by(order_id=order_id).all()