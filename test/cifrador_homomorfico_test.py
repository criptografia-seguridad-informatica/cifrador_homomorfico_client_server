from common.cifrador_homomorfico import (CifradorHomomorficoParcial)


def test_cifrador_homomorfico_encripta_un_mensaje():
    numero_a_encriptar = 5
    cifrador_homomorfico = CifradorHomomorficoParcial()
    numero_encriptado = cifrador_homomorfico.encriptar(numero_a_encriptar)
    assert numero_encriptado != numero_a_encriptar


def test_cifrador_homomorfico_desencripta_un_mensaje():
    numero_a_encriptar = 5
    cifrador_homomorfico = CifradorHomomorficoParcial()
    numero_encriptado = cifrador_homomorfico.encriptar(numero_a_encriptar)
    numero_desencriptado = cifrador_homomorfico.desencriptar(numero_encriptado)
    assert numero_a_encriptar == numero_desencriptado


def test_suma_de_dos_numeros_encriptados():
    numero_a_encriptar_1 = 10
    numero_a_encriptar_2 = 5
    operador_suma = "+"

    cifrador_homomorfico = CifradorHomomorficoParcial()

    numero_encriptado_1 = cifrador_homomorfico.encriptar(numero_a_encriptar_1)
    numero_encriptado_2 = cifrador_homomorfico.encriptar(numero_a_encriptar_2)

    suma_encriptada = cifrador_homomorfico.operaciones(numero_encriptado_1, operador_suma, numero_encriptado_2)
    suma_desencriptada = cifrador_homomorfico.desencriptar(suma_encriptada)

    assert suma_desencriptada == numero_a_encriptar_1 + numero_a_encriptar_2
