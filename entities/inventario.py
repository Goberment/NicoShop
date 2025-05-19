from sqlalchemy import Column, String, Integer, ForeignKey, DATE
from persistence.base import Base
from sqlalchemy.orm import relationship
from entities.producto import Producto

class Inventario(Base):
    __tablename__ = 'Inventario'
    id=Column(Integer, primary_key=True)
    id_producto= Column(Integer, ForeignKey('producto.id'))
    cantidad=Column(Integer)
    fecha=Column(DATE)

    producto = relationship("Producto")

