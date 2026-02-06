from aliquotas.inss_2026 import TABELA_INSS_2026

def calcular_inss(base: float) -> float:
    if base <= 0:
        return 0.0

    for faixa in TABELA_INSS_2026:
        if base <= faixa["salario_ate"]:
            return (base * faixa["aliquota"]) - faixa["parcela_deduzir"]

    ultima = TABELA_INSS_2026[-1]
    return (base * ultima["aliquota"]) - ultima["parcela_deduzir"]
