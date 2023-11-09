from modelo.cliente import Cliente
from modelo.servidor import Servidor
from modelo.cifrador_homomorfico_parcial import CifradorHomomorficoParcial

def test_cliente_servidor():
    cifrador_homomorfico_parcial = CifradorHomomorficoParcial()

    servidor = Servidor()
    cliente = Cliente(cifrador=cifrador_homomorfico_parcial)

    mensaje_enviado = cliente.enviar(5)
    mensaje_recibido = servidor.recibir_decodeado()

    servidor.enviar(mensaje_recibido)
    respuesta_recibida = cliente.recibir()

    servidor.cerrar_conexion()
    cliente.cerrar_conexion()

    assert respuesta_recibida == 5