import pytest
from descontos.inss import calcular_inss


def test_inss_base_zero():
    assert calcular_inss(0) == 0.0


def test_inss_base_negativa():
    assert calcular_inss(-1000) == 0.0


@pytest.mark.parametrize(
    "salario",
    [
        1621.00,
        2902.84,
        4354.27,
        8475.55,
    ]
)


def test_inss_limites_faixa(salario):
    desconto = calcular_inss(salario)
    assert desconto >= 0


def test_inss_acima_teto():
    desconto_teto = calcular_inss(8475.55)
    desconto_acima = calcular_inss(10000.00)
    assert desconto_acima == desconto_teto
