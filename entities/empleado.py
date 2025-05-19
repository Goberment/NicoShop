from sqlalchemy import Column, String, Integer
from persistence.base import Base

class Empleados(Base):
    __tablename__ = 'empleados'
    id=Column(Integer, primary_key=True)
    nombre=Column(String)
    puesto=Column(String)
    telefono=Column(String)
    email=Column(String)
    