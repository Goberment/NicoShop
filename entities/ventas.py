from sqlalchemy import Integer, DATE, DECIMAL, Column, ForeignKey
from persistence.base import Base
from sqlalchemy.orm import relationship
from entities.cliente import Cliente
from entities.empleado import Empleados


class Ventas(Base):
    __tablename__ = 'ventas'
    id=Column(Integer,primary_key=True)
    id_cliente=Column(Integer, ForeignKey('cliente.id') )
    id_empleado=Column(Integer, ForeignKey('empleado.id'))
    fecha=Column(DATE)
    total=Column(DECIMAL)

    cliente= relationship('Cliente')
    empleado=relationship('Empleado')
    