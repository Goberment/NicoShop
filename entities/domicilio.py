from sqlalchemy import Column, String, Integer
from persistence.base import Base

class Producto(Base):
    __tablename__ = 'domcilio'
    id=Column(Integer, primary_key=True)
    calle=Column(String)
    colonia=Column(String)
    numero_casa=Column(String)
