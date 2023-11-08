class CifradorHomomorfico:
    """
    Una clase que implementa encriptación homomórfica.
    """

    def __init__(self):
        from phe import paillier
        self.public_key, self.private_key = paillier.generate_paillier_keypair()

    def encriptar(self, numero_a_encriptar):
        return self.public_key.encrypt(numero_a_encriptar)

    def desencriptar(self):
        raise NotImplementedError("Method not yet implemented")

    def operacion(self, operacion):
        raise NotImplementedError("Method not yet implemented")