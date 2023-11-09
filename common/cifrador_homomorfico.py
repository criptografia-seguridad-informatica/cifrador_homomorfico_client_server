from phe import EncodedNumber


class CifradorHomomorficoParcial:
    """
    Una clase que implementa encriptación homomórfica.
    """

    def __init__(self):
        from phe import paillier
        from phe.encoding import EncodedNumber
        self.public_key, self.private_key = paillier.generate_paillier_keypair()

    def encriptar(self, numero_a_encriptar):
        numero_a_encriptar_encoded = EncodedNumber.encode(self.public_key, numero_a_encriptar)
        return self.public_key.encrypt(numero_a_encriptar_encoded)

    def desencriptar(self, numero_a_desencriptar):
        numero_desecriptado_encdoded = self.private_key.decrypt_encoded(numero_a_desencriptar, EncodedNumber)
        return numero_desecriptado_encdoded.decode()

    def operaciones(self, numero_1, operacion, numero_2):
        if (operacion == "+"):
            return numero_1 + numero_2
        if (operacion == "*"):
            return numero_1 * numero_2
