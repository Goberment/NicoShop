from tkinter import *
from entities.cliente import Cliente
from entities.producto import Producto
from persistence.db import SessionLocal

raiz=Tk()
raiz.mainloop()
session = SessionLocal()

def get():
     producto  = session.query(Producto).all()
     for p in producto:
          print(f"{p.id}, Nombre: {p.nombre}, Precio: ${p.precio}")

print("-----------Menú-------------")
dm= input("1.-Crear cuenta" \
"2.- Iniciar sesión" \
"3.-Mostrar Catalogo" \
"4.- Ver opciones de pago" \
"5.- ver carrito" \
"6.- ir a pagar")

while(dm=="3" or dm=="4" or dm=="5" or dm=="6"):
    if dm =="3":
         
         
         get()
         compra=input("Selecciona un producto o ()regresa al menu")
         
         while(compra=="1", compra=="2", compra=="3"):
            if compra=="1":
                print("Se agrego al carrito")
                broken=input("Quieres seleccionar algo mas 1(Si)-2(No)")
                if broken=="1":
                    break
               
                else:
                    print("regresar al menu")
                    break
                    
            if compra=="2":
                print("Se agrego al carrito")
                broken=input("Quieres seleccionar algo mas 1(Si)-2(No)")
                if broken=="1":
                    break
               
                else:
                    print("regresar al menu")
                    break
            if compra=="3":
                print("Se agrego al carrito")
                broken=input("Quieres seleccionar algo mas 1(Si)-2(No)")
                if broken=="1":
                    break
               
                else:
                    print("regresar al menu")
                    break
        
    
    
    
    
    
    


     




