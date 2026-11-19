from cupom import desconto_valido


def test_percentual_igual_ao_limite_e_aceito():
    resultado = desconto_valido(23)
    assert resultado is True


def test_percentual_acima_do_limite_e_rejeitado():
    resultado = desconto_valido(24)
    assert resultado is False


def test_percentual_zero_e_rejeitado():
    resultado = desconto_valido(0)
    assert resultado is False


def test_percentual_decimal_dentro_da_faixa_e_rejeitado():
    resultado = desconto_valido(22.5)
    assert resultado is False
