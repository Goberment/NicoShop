from entities.cliente import Cliente
from entities.producto import Producto
from persistence.db import SessionLocal

session = SessionLocal()

def get():
    producto = session.query(Producto).all()
    for p in producto:
        print(f"{p.id}, Nombre: {p.nombre}, Precio: ${p.precio}")

def save(nombre, email, password, tarjeta):
    c = Cliente(nombre=nombre, email=email, password=password, tarjeta=tarjeta)  
    session.add(c)
    session.commit()

print("-----Bienvenido a NicoShop------")

while True:
    Inicio = input("Iniciar sesion(1)---------Registrarse(2)---------: ")

    if Inicio == "1":
        correo = input("Ingresa tu correo electronico: ")
        password = input("Ingresa tu contraseña: ")

        cliente = session.query(Cliente).filter_by(email=correo, password=password).first()

        if cliente:
            carrito = []

            while True:
                print("        Menu        ")
                print("(1)Ver catalogo-(2)Ver Carrito-(3)Metodo de pago")
                entrada = input("Selecciona una opción: ")

                if entrada == "1":
                    while True:
                        get()
                        pr = input("Selecciona el ID del producto que deseas comprar: ")
                        producto_seleccionado = session.query(Producto).filter_by(id=int(pr)).first()

                        if producto_seleccionado:
                            carrito.append(producto_seleccionado)
                            print("Se agregó al carrito:", producto_seleccionado.nombre)
                        else:
                            print("Producto no encontrado.")

                        sl = input("¿Quieres seguir comprando? si(1) - no(2): ")
                        if sl == "2":
                            print("\n------ Productos en tu carrito ------")
                            total = 0
                            for prod in carrito:
                                print(f"{prod.nombre} - {prod.descripcion} - ${prod.precio}")
                                total += float(prod.precio)

                            print(f"Total a pagar: ${total}")
                            break

                elif entrada == "2":
                    print("Carrito actual:")
                    if carrito:
                        for prod in carrito:
                            print(f"{prod.nombre} - ${prod.precio}")
                    else:
                        print("Tu carrito está vacío.")

                elif entrada == "3":
                    print("Opciones de pago:\n1. Tarjeta\n2. Deposito OXXO")
                    metodo = input("Selecciona el método de pago (1 o 2): ")

                    if metodo == "1":
                        print(f"Tu tarjeta registrada es: {cliente.tarjeta}")
                        usar = input("¿Quieres usar esta tarjeta? (1 = Sí / 2 = No): ")
                        if usar == "1":
                            print("Compra exitosa.")
                        elif usar == "2":
                            nueva_tarjeta = input("Introduce el nuevo número de tarjeta: ")
                            cliente.tarjeta = nueva_tarjeta
                            session.commit()
                            print("Tarjeta actualizada y compra exitosa.")
                        else:
                            print("Opción no válida.")
                    elif metodo == "2":
                        print("Generando código de barras para pago en OXXO...")
                        print('|||| |||| || ||||| || | | | ||||') 
                    else:
                        print("Opción de pago no válida.")
        else:
            print("Credenciales incorrectas. Intenta nuevamente.")

    elif Inicio == "2":
        nombre = input("Ingresa su nombre: ")
        email = input("Ingresa su correo electronico: ")
        password = input("Ingresa una contraseña: ")
        tarjeta = input("Ingresa tu número de tarjeta: ")
        save(nombre, email, password, tarjeta)
        print("Cuenta creada con éxito. Vuelve a iniciar sesión.")
    else:
        print("Crea una cuenta")
