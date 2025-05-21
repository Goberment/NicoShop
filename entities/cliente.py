from sqlalchemy import Column, Integer, String
from persistence.base import Base

class Cliente(Base):
    __tablename__ = 'cliente'
    id=Column(Integer, primary_key=True)
    nombre=Column(String)
    email=Column(String)
    password=Column(String)
    tarjeta = Column(String) # se agrego tarjeta
    
