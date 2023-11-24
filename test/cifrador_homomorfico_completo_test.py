from modelo.cifrador_homomorfico_completo import CifradorHomomorficoCompleto

def test_cifrador_homomorfico_completo_encripta_un_mensaje():
    numero_a_encriptar = 5
    cifrador_homomorfico = CifradorHomomorficoCompleto()
    numero_encriptado = cifrador_homomorfico.encriptar(numero_a_encriptar)
    assert numero_encriptado != numero_a_encriptar

def test_cifrador_homomorfico_completo_desencripta_un_mensaje():
    numero_a_encriptar = 5
    cifrador_homomorfico_completo = CifradorHomomorficoCompleto()
    numero_encriptado = cifrador_homomorfico_completo.encriptar(numero_a_encriptar)
    numero_desencriptado = cifrador_homomorfico_completo.desencriptar(numero_encriptado)
    assert numero_a_encriptar == numero_desencriptado

def test_suma_de_un_numero_encriptado_y_uno_no_encriptado():
    numero_a_encriptar = 10
    numero_no_encriptado = 5

    cifrador_homomorfico_completo = CifradorHomomorficoCompleto()

    numero_encriptado = cifrador_homomorfico_completo.encriptar(numero_a_encriptar)

    suma_encriptada = numero_encriptado + numero_no_encriptado
    suma_desencriptada = cifrador_homomorfico_completo.desencriptar(suma_encriptada)

    assert suma_desencriptada == 15

def test_suma_de_dos_numeros_encriptados():
    numero_a_encriptar_1 = 10
    numero_a_encriptar_2 = 5

    cifrador_homomorfico_completo = CifradorHomomorficoCompleto()

    numero_encriptado_1 = cifrador_homomorfico_completo.encriptar(numero_a_encriptar_1)
    numero_encriptado_2 = cifrador_homomorfico_completo.encriptar(numero_a_encriptar_2)

    suma_encriptada = numero_encriptado_1 + numero_encriptado_2
    suma_desencriptada = cifrador_homomorfico_completo.desencriptar(suma_encriptada)

    assert suma_desencriptada == 15


def test_multiplicacion_de_un_numero_encriptado_por_numero_no_encriptado():
    numero_a_encriptar_1 = 5
    numero_2 = 5

    cifrador_homomorfico_completo = CifradorHomomorficoCompleto()
    numero_encriptado_1 = cifrador_homomorfico_completo.encriptar(numero_a_encriptar_1)
    multiplicacion_encriptada = numero_encriptado_1 * numero_2
    multiplicacion_desencriptada = cifrador_homomorfico_completo.desencriptar(multiplicacion_encriptada)

    assert multiplicacion_desencriptada == 25
