from modelo.cliente import Cliente

cliente = Cliente()

print('Conectado a {}:{}'.format(*cliente.direccion_servidor))

while True:
    mensaje = input('Escribir mensaje ("exit" para terminar): ')

    cliente.enviar(mensaje)

    if mensaje.lower() == 'exit':
        break

    data = cliente.recibir()
    print('Respuesta del servidor:', data)

cliente.cerrar_conexion()