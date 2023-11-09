from cliente import Cliente

if __name__ == '__main__':
    cliente = Cliente()

    message = input("Escribir un mensaje: ")
    cliente.enviar_mensaje(message)

    received_message = cliente.recibir_mensaje()

    print("El servidor devolvió: ", received_message)

    cliente.cerrar_conexion()
