MAXIMO = 23


def desconto_valido(percentual):
    if percentual <= 0:
        return False
    if percentual != int(percentual):
        return False
    return percentual <= MAXIMO
