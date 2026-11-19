MAXIMO = 23


def desconto_valido(percentual):
    if percentual <= 0:
        return False
    return percentual <= MAXIMO
