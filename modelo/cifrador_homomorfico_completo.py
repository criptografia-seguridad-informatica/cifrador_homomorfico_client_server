from Pyfhel import Pyfhel
import numpy as np
class CifradorHomomorficoCompleto:
    """
    Una clase que implementa encriptación homomórfica completa.
    """

    def __init__(self):
        fhe = Pyfhel()
        fhe.contextGen(scheme='bfv', n=2**14, t_bits=20)
        fhe.keyGen()
        self.__fhe = fhe

    def encriptar(self, numero_a_encriptar):
        integer = np.array([numero_a_encriptar], dtype=np.int64)
        return self.__fhe.encryptInt(integer)


    def desencriptar(self, numero_a_desencriptar):
        return self.__fhe.decryptInt(numero_a_desencriptar)[0]
