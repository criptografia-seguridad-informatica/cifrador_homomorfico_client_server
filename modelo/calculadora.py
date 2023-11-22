class Calculadora:
    def __init__(self, expression):
        self.__expression = expression

    def calcular(self):
        from phe.paillier import EncryptedNumber

        numeros = []
        operadores = []

        for item in self.__expression:
            if isinstance(item, (int, float, EncryptedNumber)):
                numeros.append(item)
            elif item in {'+', '-', '*', '/'}:
                operadores.append(item)
            else:
                raise ValueError(f"Item invalido: {item}")

            while len(numeros) >= 2 and len(operadores) >= 1:
                num2 = numeros.pop()
                num1 = numeros.pop()
                operador = operadores.pop()

                if operador == '+':
                    resultado = num1 + num2
                elif operador == '-':
                    resultado = num1 - num2
                elif operador == '*':
                    resultado = num1 * num2
                elif operador == '/':
                    resultado = num1 / num2
                else:
                    raise ValueError(f"Operador Invalido: {operador}")

                numeros.append(resultado)

        if len(numeros) == 1:
            return numeros[0]
        else:
            raise ValueError("Invalid expression")
