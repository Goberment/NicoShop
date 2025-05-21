from entities.cliente import Cliente
from entities.producto import Producto
from persistence.db import SessionLocal

session = SessionLocal()

def get():
    producto = session.query(Producto).all()
    for p in producto:
        print(f"{p.id}, Nombre: {p.nombre}, Precio: ${p.precio}")

def guardar(self):
    try:
        session.add(self)
        session.commit()
        print("se guardo correctamente")
    except Exception as e:
        session.rollback()
        print("Error al guardar los datos")


print("-----Bienvenido a NicoShop------")

Inicio=input("Iniciar sesión(1)---------Registrarse(2)---------")

if Inicio=="1":
    correo=input("Ingresa tu correo electronico: ")
    password=input("Ingresa tu contraseña: ")



elif(Inicio=="2"):
    name=input("Ingresa su nombre: ")
    correo=input("Ingresa su correo electronico: ")
    password=input("Ingresa una contraseña: ")

    