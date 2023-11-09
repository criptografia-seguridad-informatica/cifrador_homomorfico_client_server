from modelo.cliente import Cliente

if __name__ == '__main__':
    cliente = Cliente()

    mensaje = input("Escribir un mensaje: ")
    cliente.enviar(mensaje)

    received_message = cliente.recibir()

    print("El servidor devolvió: ", received_message)

    cliente.cerrar_conexion()
