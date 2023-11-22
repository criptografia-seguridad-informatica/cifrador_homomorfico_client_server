from argparse import ArgumentParser
from modelo.cliente import Cliente
from modelo.cifrador_homomorfico_parcial import CifradorHomomorficoParcial


def init_args():
    parser = ArgumentParser(description="Flags para activar o los tipos de cifradores")
    parser.add_argument("--phe", help="Activa el cifrador homomorfico parcial", action="store_true")
    args = parser.parse_args()
    return args


def main():
    args = init_args()

    cifrador = None
    if args.phe:
        cifrador = CifradorHomomorficoParcial()

    cliente = Cliente(cifrador)

    print('Conectado a {}:{}'.format(*cliente.direccion_servidor))

    while True:
        mensaje = input('Escribir expresión ("exit" para terminar): ')

        if mensaje.lower() == 'exit':
            break
        try:
            cliente.enviar(mensaje)
        except AttributeError:
            print('No hay ningún cifrador configurado.')
            break

        data = cliente.recibir()
        print('Resultado del servidor:', data)

    cliente.cerrar_conexion()


if __name__ == "__main__":
    main()
