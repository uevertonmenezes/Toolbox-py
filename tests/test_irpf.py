from descontos.irpf import calcular_irpf
from aliquotas.irpf_2026 import TABELA_IRPF_2026, ABATIMENTO_ISENCAO_2026


def test_irpf_base_zero():
    assert calcular_irpf(0) == 0.0


def test_irpf_base_negativa():
    assert calcular_irpf(-1000) == 0.0


def test_irpf_isencao_ate_5000():
    # Mesmo que a tabela gere imposto,o abatimento 2026 deve zerar.
    assert calcular_irpf(5000) == 0.0


def test_irpf_primeira_faixa_tributavel():
    base = 5500
    imposto = calcular_irpf(base)
    assert imposto > 0


def test_irpf_limite_exato_faixa():
    faixa = TABELA_IRPF_2026[0]
    base = faixa["base_ate"]
    imposto = calcular_irpf(base)

    esperado = (base * faixa["aliquota"]) - faixa["parcela_deduzir"]
    esperado -= ABATIMENTO_ISENCAO_2026
    assert round(imposto, 2) == round(max(esperado, 0), 2)


def test_irpf_ultima_faixa():
    base = 12000
    imposto = calcular_irpf(base)
    assert imposto > 0


def test_irpf_nunca_negativo():
    # Mesmo após abatimento, nunca pode retornar um valor negativo.
    base = 5100
    imposto = calcular_irpf(base)
    assert imposto >= 0
