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
            carrito = []  # se crea una lista vacía para almacenar productos seleccionados

            while True:
                print("        Menu        ")
                print("(1)Ver catalogo-(2)Ver Carrito-(3)Metodo de pago")
                entrada = input("Selecciona una opción: ")

                if entrada == "1":
                    while True:  # ciclo para seguir comprando hasta que el usuario decida parar
                        get()
                        pr = input("Selecciona el ID del producto que deseas comprar: ")
                        producto_seleccionado = session.query(Producto).filter_by(id=int(pr)).first()

                        if producto_seleccionado:
                            carrito.append(producto_seleccionado)  # se agrega el producto a la lista
                            print("Se agregó al carrito:", producto_seleccionado.nombre)
                        else:
                            print("Producto no encontrado.")

                        sl = input("¿Quieres seguir comprando? si(1) - no(2): ")
                        if sl == "2":
                            print("\n------ Productos en tu carrito ------")
                            total = 0
                            for prod in carrito:
                                print(f"{prod.nombre} - {prod.descripcion} - ${prod.precio}")
                                total += float(prod.precio)  # se convierte a número para la suma

                            print(f"Total a pagar: ${total}")
                            print("¿Deseas ir a pagar? (Sí o No)")  # mensaje final para ir a pagar
                            break  # se sale del ciclo de compras

                elif entrada == "2":
                    print("Carrito actual:")
                    if carrito:
                        for prod in carrito:
                            print(f"{prod.nombre} - ${prod.precio}")
                    else:
                        print("Tu carrito está vacío.")

                elif entrada == "3":
                    print("Opciones de pago: Tarjeta, Transferencia o Pago en tienda")

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
