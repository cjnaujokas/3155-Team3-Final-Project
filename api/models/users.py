<<<<<<< Updated upstream
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class User(Base):
    __tablename__ = "users"

    # Columns
    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)  
    password = Column(String(100), nullable=False)  
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=True) 

    # Relationships
    orders = relationship("Order", back_populates="user")  

    def __repr__(self):
        return f"<User(user_id={self.user_id}, order_id={self.order_id})>"

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "order_id": self.order_id,
        }

    # CRUD Operations
    @classmethod
    def create_user(cls, session, password: str, order_id: int = None):
        """
        Create a new user.
        TODO: Implement logic to create a new user.
        """
        pass

    @classmethod
    def update_user(cls, session, user_id: int, **kwargs):
        """
        Update an existing user's details.
        TODO: Implement logic to update a user's information.
        """
        pass

    @classmethod
    def delete_user(cls, session, user_id: int):
        """
        Delete a user by their ID.
        TODO: Implement logic to delete a user.
        """
        pass

    @classmethod
    def get_user_by_id(cls, session, user_id: int):
        """
        Retrieve a specific user by their ID.
        TODO: Implement logic to fetch a user by ID.
        """
        pass

    @classmethod
    def get_all_users(cls, session):
        """
        Retrieve all users.
        TODO: Implement logic to fetch all users.
        """
        pass
=======
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)

    # Relationships
    orders = relationship("Order", back_populates="user", cascade="all, delete-orphan")
>>>>>>> Stashed changes
