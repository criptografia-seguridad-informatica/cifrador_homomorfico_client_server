from modelo.calculadora import Calculadora
from modelo.cifrador_homomorfico_parcial import CifradorHomomorficoParcial

def test_vector_con_numeros_enteros():
    expresion = [1,'-',2,'+',3,'+',5,'-',2]

    calculadora = Calculadora(expresion)
    resultado = calculadora.calcular()
    assert resultado == 5

def test_vector_con_cifrado_homomorfico_parcial():
    cifrador = CifradorHomomorficoParcial()
    e1 = cifrador.encriptar(1)
    e2 = cifrador.encriptar(2)
    e3 = cifrador.encriptar(3)
    e5 = cifrador.encriptar(5)

    expresion = [e1, '-', e2, '+', e3, '+', e5, '-', e2]

    calculadora = Calculadora(expresion)
    resultado_encriptado = calculadora.calcular()

    resultado_desencriptado = cifrador.desencriptar(resultado_encriptado)

    assert resultado_desencriptado == 5
