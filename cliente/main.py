from cliente import Cliente
from socket import socket

if __name__ == '__main__':
    cliente = Cliente()

    mensaje = input("Escribir un mensaje: ")
    cliente.enviar_mensaje(mensaje)

    received_message = cliente.recibir_mensaje()

    print("El servidor devolvió: ", received_message)

    cliente.cerrar_conexion()
