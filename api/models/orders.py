from sqlalchemy import Column, Boolean,ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from datetime import datetime
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(String(100))
    order_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    description = Column(String(300), nullable=True)
    takeout = Column(Boolean, nullable=False, default=False)

    order_details = relationship("OrderDetail", back_populates="order", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Order(id={self.id}, customer_name={self.customer_name}, order_date={self.order_date}, description={self.description}, takeout={self.takeout})>"
    
    def to_dict(self):
        return {
            "id": self.id,
            "customer_name": self.customer_name,
            "order_date": self.order_date,
            "description": self.description,
            "takeout": self.takeout
        }
    
        #CRUD
    @classmethod
    def create_order(cls, session: Session, customer_name: str, description: str, takeout: bool):
        #creates new order
        try:
            new_order = cls(customer_name=customer_name,description=description,takeout=takeout)
            session.add(new_order)
            session.commit()
            return new_order
        except Exception as e:
            session.rollback()
            raise e
        
    @classmethod   
    def get_orderID(cls, session: Session, orderid: int):
        #gets order by id
            return session.query(cls).filter_by(id=orderid).first()
    
    @classmethod
    def update_order(cls, session: Session, order_id: int, **kwargs):
        #updates order
        try:
            order = session.query(cls).filter_by(id=order_id).first()
            if not order:
                raise ValueError(f"Order with ID {order_id} does not exist.")
            for key, value in kwargs.items():
                if hasattr(order, key):
                    setattr(order, key, value)
            session.commit()
            return order
        except Exception as e:
            session.rollback()
            raise e
        
    @classmethod
    def delete_order(cls, session: Session, order_id: int):
      #deletes an order
        try:
            order = session.query(cls).filter_by(id=order_id).first()
            if order:
                session.delete(order)
                session.commit()
            else:
                raise ValueError(f"Order with ID {order_id} does not exist.")
        except Exception as e:
            session.rollback()
            raise e

    @classmethod
    def list_orders(cls, session: Session):
        #list all orders
        return session.query(cls).all()