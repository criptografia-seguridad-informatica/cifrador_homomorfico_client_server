import socket
from modelo.cifrador_homomorfico_parcial import CifradorHomomorficoParcial


class Cliente:
    def __init__(self, socket_cliente: socket = socket.socket(),
                 host='localhost',
                 port=5000):

        self.__cifrador = None
        self.__socket = socket_cliente
        self.__socket.connect((host, port))

    def enviar(self, mensaje):
        if not self.__cifrador:
            mensaje_a_enviar = mensaje.encode()
        else:
            mensaje_a_enviar = self.__cifrador.encriptar(mensaje)
        self.__socket.send(mensaje_a_enviar)
        return mensaje_a_enviar

    def recibir(self):
        return self.__socket.recv(1024).decode()

    def cerrar_conexion(self):
        self.__socket.shutdown(socket.SHUT_RDWR)
        self.__socket.close()
