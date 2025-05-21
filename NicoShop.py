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
    c = Cliente(nombre=nombre, email=email, password=password, tarjeta=tarjeta)  # ahora guarda también la tarjeta
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

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('nicolasbecerramuro@gmail.com', 'yspqnoofirxbjvwi')
            smtp.send_message(msg)

        print("Correo de bienvenida enviado con éxito.")
    except Exception as e:
        print("No se pudo enviar el correo:", e)

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
                            print("¿Deseas ir a pagar? (Sí o No)")
                            break

                elif entrada == "2":
                    print("Carrito actual:")
                    if carrito:
                        for prod in carrito:
                            print(f"{prod.nombre} - ${prod.precio}")
                    else:
                        print("Tu carrito está vacío.")

                elif entrada == "3":
                    print("Opciones de pago:\n(1) Tarjeta\n(2) Depósito OXXO")
                    metodo = input("Selecciona el método de pago (1 o 2): ")

                    if metodo == "1":
                        print(f"Tu tarjeta registrada es: {cliente.tarjeta}")
                        usar = input("¿Deseas usar esta tarjeta? (1: Sí, 2: No): ")
                        if usar == "1":
                            print("Compra exitosa con tu tarjeta registrada.")
                        elif usar == "2":
                            nueva_tarjeta = input("Ingresa el nuevo número de tarjeta: ")
                            cliente.tarjeta = nueva_tarjeta
                            session.commit()
                            print("Tarjeta actualizada y compra exitosa.")
                        else:
                            print("Opción no válida.")

                    elif metodo == "2":
                        print("Realiza tu pago en OXXO con el siguiente código:")
                        print("|| 1234 5678 9012 3456 ||")  # Código simulado tipo código de barras
                        print("Compra registrada. Recibirás confirmación cuando se confirme el pago.")

        else:
            print("Credenciales incorrectas. Intenta nuevamente.")

    elif Inicio == "2":
        nombre = input("Ingresa su nombre: ")
        email = input("Ingresa su correo electronico: ")
        password = input("Ingresa una contraseña: ")
        tarjeta = input("Ingresa tu número de tarjeta: ")  # NUEVO CAMPO requerido en el registro
        save(nombre, email, password, tarjeta)
        enviar_correo_bienvenida(email)
        print("Cuenta creada con éxito. Vuelve a iniciar sesión.")
    else:
        print("Crea una cuenta")

