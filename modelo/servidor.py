import socket
import pickle


class Servidor:
    def __init__(self, socket_servidor: socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM), host='0.0.0.0',
                 puerto=5000):
        self.direccion_servidor = (host, puerto)
        self.__socket_servidor = socket_servidor
        self.__socket_servidor.bind((host, puerto))
        self.__socket_servidor.listen(1)
        self.__socket_cliente = None
        self.direccion_cliente = None

    def aceptar_conexion(self):
        self.__socket_cliente, self.direccion_cliente = self.__socket_servidor.accept()
        return self.direccion_cliente

    def recibir(self):
        datos_recibidos = self.__socket_cliente.recv(4096)
        return pickle.loads(datos_recibidos)

    def enviar(self, mensaje):
        mensaje_a_enviar = pickle.dumps(mensaje)
        self.__socket_cliente.sendall(mensaje_a_enviar)

    def cerrar_conexion(self):
        self.__socket_servidor.close()
        self.__socket_cliente.close()
