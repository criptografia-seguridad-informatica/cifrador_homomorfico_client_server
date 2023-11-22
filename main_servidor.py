from modelo.servidor import Servidor
from modelo.calculadora import Calculadora

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


    calculadora = Calculadora(data)
    resultado = calculadora.calcular()

    servidor.enviar(resultado)

servidor.cerrar_conexion()
