from entities.cliente import Cliente
from entities.producto import Producto
from persistence.db import SessionLocal

session = SessionLocal()

def get():
    producto = session.query(Producto).all()
    for p in producto:
        print(f"{p.id}, Nombre: {p.nombre}, Precio: ${p.precio}")

def save(nombre, email, password):
    c = Cliente(nombre=nombre, email=email, password=password)  
    session.add(c)
    session.commit()

print("-----Bienvenido a NicoShop------")

while True:  # aqui se agrega bucle para que regrese al menú después del registro
    Inicio = input("Iniciar sesion(1)---------Registrarse(2)---------: ")

    if Inicio == "1":
        correo = input("Ingresa tu correo electronico: ")
        password = input("Ingresa tu contraseña: ")

        # validación con base de datos para verificar si el cliente existe
        cliente = session.query(Cliente).filter_by(email=correo, password=password).first()

        if cliente:  # si se encontró el cliente, se permite continuar
            while True:
                print("        Menu        ")
                print("(1)Ver catalogo-(2)Ver Carrito-(3)Metodo de pago")
                entrada = input("Selecciona una opción: ")

                if entrada == "1":
                    print("hellow")
                    get()
                    pr = input("Selecciona un producto: ")

                    if pr == "1":
                        print("Se agrego al carrito")
                        sl = input("Quieres seguir comprando si(1)-no(2): ")
                        if sl == "1":
                            break
                        elif sl == "2":
                            break
                    if pr == "2":
                        print("Se agrego al carrito")
                        sl = input("Quieres seguir comprando si(1)-no(2): ")
                        if sl == "1":
                            break
                        elif sl == "2":
                            break
                    if pr == "3":
                        print("Se agrego al carrito")
                        sl = input("Quieres seguir comprando si(1)-no(2): ")
                        if sl == "1":
                            break
                        elif sl == "2":
                            break
               
        else:
            print("Credenciales incorrectas. Intenta nuevamente.")  # mensaje de error si el login falla

    elif Inicio == "2":
        nombre = input("Ingresa su nombre: ")
        email = input("Ingresa su correo electronico: ")
        password = input("Ingresa una contraseña: ")
        save(nombre, email, password)
        print("Cuenta creada con éxito. Vuelve a iniciar sesión.")  # mensaje de confirmación de que la nueva cuenta fue creada con exito
    else:
        print("Crea una cuenta")
