from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from datetime import datetime
from ..dependencies.database import Base

class Promo_Codes(Base):
    __tablename__ = "promotions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    code = Column(Integer, unique=True)
    expiration = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    description = Column(String(300), nullable=True)