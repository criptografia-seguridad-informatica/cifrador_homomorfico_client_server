class Cliente:
    """

    """
    def __init__(self, host = 'localhost', port = 5000):
        from socket import socket

        client_socket = socket()
        client_socket.connect((host,port))

        self._socket = client_socket
    def enviar_mensaje(self, message):
        self._socket.send(message.encode())

    def recibir_mensaje(self):
        return self._socket.recv(1024).decode()

    def cerrar_conexion(self):
        self._socket.close()