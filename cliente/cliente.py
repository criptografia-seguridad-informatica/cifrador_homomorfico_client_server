from socket import socket


class Cliente:
    """

    """

    def __init__(self, socket_cliente: socket = socket(), host='localhost', port=5000):
        socket_cliente.connect((host, port))
        self._socket = socket_cliente

    def enviar_mensaje(self, message):
        self._socket.send(message.encode())

    def recibir_mensaje(self):
        return self._socket.recv(1024).decode()

    def cerrar_conexion(self):
        self._socket.close()
