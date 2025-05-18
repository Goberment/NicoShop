from sqlalchemy import Column, String, Integer
from persistence.base import Base

class Producto(Base):
    __tablename__ = 'producto'
    id=Column(Integer, primary_key=True)
    nombre=Column(String)
    descripcion=Column(String)
    precio=Column(String)
