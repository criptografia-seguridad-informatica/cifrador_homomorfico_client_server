import socket
import pickle
from modelo.cifrador_homomorfico_parcial import CifradorHomomorficoParcial
from helpers.helpers import tokenizar_expresion


class Cliente:
    def __init__(self, cifrador: CifradorHomomorficoParcial = None,
                 socket_cliente: socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM),
                 host='localhost',
                 port=5000):
        self.direccion_servidor = (host, port)
        self.__cifrador = cifrador
        self.__socket = socket_cliente
        self.__socket.connect((host, port))

    def convertir(self, token):
        if token[0] == 'e':
            return self.__cifrador.encriptar(float(token[1:]))
        elif token.isdigit():
            return float(token)
        return token

    def enviar(self, mensaje):
        try:
            tokens = tokenizar_expresion(mensaje)
            mensaje = [self.convertir(token) for token in tokens]
        except ValueError:
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
