from modelo.servidor import Servidor

servidor = Servidor()
print('Servidor escuchando en {}:{}'.format(*servidor.direccion_servidor))

direccion_cliente = servidor.aceptar_conexion()
print('Conexión establecida con: ', direccion_cliente)

while True:
    data = servidor.recibir()
    if not data or data.lower() == 'exit':
        break

    print('Mensaje del cliente:', data)

    servidor.enviar(data)

servidor.cerrar_conexion()
