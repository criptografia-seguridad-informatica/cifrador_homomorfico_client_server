from modelo.servidor import Servidor

def server_program():
    print("Servidor comenzado")

    servidor = Servidor()

    mensaje_recibido = servidor.recibir_decodeado()

    print("Se recibio el mensaje:", mensaje_recibido)

    servidor.enviar(mensaje_recibido)

    servidor.cerrar_conexion()

if __name__ == '__main__':
    server_program()
