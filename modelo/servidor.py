import socket


class Servidor:
    def __init__(self, socket_servidor: socket = socket.socket(), host='', port=5000):
        self.__socket = socket_servidor
        self.__socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.__socket.bind((host, port))
        self.__socket.listen(1)
        self.__client_socket = None

    def recibir(self):
        self.__client_socket, _client_address = self.__socket.accept()
        return self.__client_socket.recv(1024)

    def recibir_decodeado(self):
        self.__client_socket, _client_address = self.__socket.accept()
        return self.__client_socket.recv(1024).decode()

    def enviar(self, mensaje_a_enviar):
        self.__client_socket.send(mensaje_a_enviar.encode())

    def cerrar_conexion(self):
        self.__socket.shutdown(socket.SHUT_RDWR)
        self.__socket.close()
        self.__client_socket.close()
