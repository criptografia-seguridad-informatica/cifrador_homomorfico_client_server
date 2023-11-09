import socket
import pickle
from modelo.cifrador_homomorfico_parcial import CifradorHomomorficoParcial


class Cliente:
    def __init__(self, cifrador: CifradorHomomorficoParcial = None, socket_cliente: socket = socket.socket(),
                 host='localhost',
                 port=5000):
        self.__cifrador = cifrador
        self.__socket = socket_cliente
        self.__socket.connect((host, port))

    def enviar(self, mensaje):
        if self.__cifrador:
            mensaje = self.__cifrador.encriptar(mensaje)

        mensaje_a_enviar = pickle.dumps(mensaje)
        self.__socket.send(mensaje_a_enviar)
        return mensaje_a_enviar

    def recibir(self):
        datos_recibidos = self.__socket.recv(4096)
        objeto_recibido = pickle.loads(datos_recibidos)
        if self.__cifrador:
            objeto_recibido = self.__cifrador.desencriptar(objeto_recibido)
        return objeto_recibido

    def cerrar_conexion(self):
        self.__socket.close()
