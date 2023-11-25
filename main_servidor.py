import logging

from modelo.servidor import Servidor
from modelo.calculadora import Calculadora
logging.basicConfig(level=logging.INFO)

servidor = Servidor()
print('Servidor escuchando en {}:{}'.format(*servidor.direccion_servidor))

direccion_cliente = servidor.aceptar_conexion()
print('Conexión establecida con: ', direccion_cliente)

while True:
    try:
        data = servidor.recibir()
    except EOFError:
        break

    print('Mensaje del cliente:', data)

    import pdb
    calculadora = Calculadora(data)

    pdb.set_trace()
    try:
        resultado = calculadora.calcular()
    except ValueError:
        print("Item para calcular invalido")
        break

    servidor.enviar(resultado)

servidor.cerrar_conexion()
