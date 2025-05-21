from entities.cliente import Cliente
from entities.producto import Producto
from persistence.db import SessionLocal

session = SessionLocal()

def get():
    producto = session.query(Producto).all()
    for p in producto:
        print(f"{p.id}, Nombre: {p.nombre}, Precio: ${p.precio}")

def save(nombre, email, password):
    c=Cliente   (nombre=nombre, email=email, password=password)  
    session.add(c)
    session.commit()


print("-----Bienvenido a NicoShop------")

Inicio=input("Iniciar sesión(1)---------Registrarse(2)---------: ")

if Inicio=="1":
    correo=input("Ingresa tu correo electronico: ")
    password=input("Ingresa tu contraseña: ")



elif(Inicio=="2"):
    nombre=input("Ingresa su nombre: ")
    email=input("Ingresa su correo electronico: ")
    password=input("Ingresa una contraseña: ")
    save(nombre, email, password)

else:
    print("Crea una cuenta")

    