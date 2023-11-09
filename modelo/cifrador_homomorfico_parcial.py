class CifradorHomomorficoParcial:
    """
    Una clase que implementa encriptación homomórfica.
    """

    def __init__(self):
        from phe import paillier
        from phe import EncodedNumber

        self.__encoder = EncodedNumber
        self.__public_key, self.private_key = paillier.generate_paillier_keypair()

    def encriptar(self, numero_a_encriptar):
        numero_a_encriptar_encoded = self.__encoder.encode(self.__public_key, numero_a_encriptar)
        return self.__public_key.encrypt(numero_a_encriptar_encoded)

    def desencriptar(self, numero_a_desencriptar):
        numero_desencriptado_encoded = self.private_key.decrypt_encoded(numero_a_desencriptar, self.__encoder)
        return numero_desencriptado_encoded.decode()
