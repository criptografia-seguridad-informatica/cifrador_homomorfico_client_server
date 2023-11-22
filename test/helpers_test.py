import pytest
from helpers.helpers import tokenizar_expresion


def test_tokenizador_devuelve_tokens_como_lista():
    expresion = "e5+9+e10*e15"

    tokens = tokenizar_expresion(expresion)

    assert ['e5', '+', '9', '+', 'e10', '*', 'e15'] == tokens


def test_si_no_es_una_expresion_lanza_error():
    with pytest.raises(ValueError):
        expresion = "Hola mundo"
        tokenizar_expresion(expresion)
