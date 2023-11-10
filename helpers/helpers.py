import re


def tokenizar_expresion(expression):
    tokens = re.findall(r'([a-zA-Z]*\d+|[+\-*/()])', expression)

    if not tokens:
        raise ValueError("No valid tokens found in the expression")

    return tokens
