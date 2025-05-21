import smtplib
from email.message import EmailMessage

from entities.cliente import Cliente
from entities.producto import Producto
from persistence.db import SessionLocal

session = SessionLocal()

def get():
    producto = session.query(Producto).all()
    for p in producto:
        print(f"{p.id}, Nombre: {p.nombre}, Precio: ${p.precio}")

def save(nombre, email, password, tarjeta):
    c = Cliente(nombre=nombre, email=email, password=password, tarjeta=tarjeta)  # se agrega la tarjeta al cliente
    session.add(c)
    session.commit()

# Función para enviar correo de bienvenida al usuario registrado
def enviar_correo_bienvenida(destinatario):
    try:
        msg = EmailMessage()
        msg['Subject'] = 'Bienvenido a NicoShop'
        msg['From'] = 'nicolasbecerramuro'
        msg['To'] = destinatario
        msg.set_content('Gracias por registrarte en NicoShop. ¡Disfruta tus compras!')

        # Conexión con el servidor SMTP de Gmail
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('nicolasbecerramuro@gmail.com', 'yspqnoofirxbjvwi')  # correo personal y contraseña de aplicación
            smtp.send_message(msg)

        print("Correo de bienvenida enviado con éxito.")
    except Exception as e:
        print("No se pudo enviar el correo:", e)

print("-----Bienvenido a NicoShop------")

while True:  # aqui se agrega bucle para que regrese al menú después del registro
   
    print("1.-Inicio sesion")
    print("2,.Registrarse")

    Inicio = input("Selecciona una opción: ")

    if Inicio == "1":
        correo = input("Ingresa tu correo electronico: ")
        password = input("Ingresa tu contraseña: ")

        # validación con base de datos para verificar si el cliente existe
        cliente = session.query(Cliente).filter_by(email=correo, password=password).first()

        if cliente:  # si se encontró el cliente, se permite continuar
            carrito = []  # lista vacía para almacenar productos seleccionados

            while True:
                print("        Menu        ")
                print("(1)Ver catalogo")
                print("2,.Ver carrito")
                print("3.-Metodo de pago")
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

                        if sl == "3":
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
            print("Credenciales incorrectas. Intenta nuevamente.") 

    elif Inicio == "2":
        nombre = input("Ingresa su nombre: ")
        email = input("Ingresa su correo electronico: ")
        password = input("Ingresa una contraseña: ")
        tarjeta = input("Ingresa tu número de tarjeta: ")  
        save(nombre, email, password, tarjeta)
        enviar_correo_bienvenida(email)  # Aquí se envía el correo 
        print("Cuenta creada con éxito. Vuelve a iniciar sesión.")  # mensaje de creacion de cuenta correctamente 
    else:
        print("Crea una cuenta")