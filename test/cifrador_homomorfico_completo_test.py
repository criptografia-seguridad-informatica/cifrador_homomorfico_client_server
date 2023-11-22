from modelo.cifrador_homomorfico_completo import CifradorHomomorficoCompleto



def test_cifrador_homomorfico_encripta_un_mensaje():
    numero_a_encriptar = 5
    cifrador_homomorfico = CifradorHomomorficoCompleto()
    numero_encriptado = cifrador_homomorfico.encriptar(numero_a_encriptar)
    assert numero_encriptado != numero_a_encriptar
