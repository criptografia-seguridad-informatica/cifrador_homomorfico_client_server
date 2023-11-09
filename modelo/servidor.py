import socket
import pickle


class Servidor:
    def __init__(self, socket_servidor: socket = socket.socket(), host='', port=5000):
        self.__socket = socket_servidor
        self.__socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.__socket.bind((host, port))
        self.__socket.listen(1)
        self.__client_socket = None

    def recibir(self):
        self.__client_socket, _client_address = self.__socket.accept()
        return self.__client_socket.recv(4096)

    def recibir_decodeado(self):
        self.__client_socket, _client_address = self.__socket.accept()
        datos_recibidos = self.__client_socket.recv(4096)
        return pickle.loads(datos_recibidos)

    def enviar(self, mensaje):
        mensaje_a_enviar = pickle.dumps(mensaje)
        self.__client_socket.send(mensaje_a_enviar)

    def cerrar_conexion(self):
        self.__socket.shutdown(socket.SHUT_RDWR)
        self.__socket.close()
        self.__client_socket.close()
