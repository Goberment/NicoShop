from sqlalchemy import Integer, String, ForeignKey, DECIMAL, Date, Column
from persistence.base import Base
from sqlalchemy.orm import relationship
from entities.ventas import Ventas
from entities.producto import Producto

class Detalle(Base):
    id=Column(Integer, primary_key=True)
    id_venta=Column(Integer, ForeignKey('ventas'))
    id_producto=Column(Integer, ForeignKey('producto'))
    cantidad=Column(Integer)
    precio_unitario=Column(DECIMAL)

    ventas=relationship('Ventas')
    producto=relationship('Producto')
