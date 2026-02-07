from aliquotas.irpf_2026 import TABELA_IRPF_2026

def calcular_irpf(base: float) -> float:
    if base <= 0:
        return 0.0

    for faixa in TABELA_IRPF_2026:
        if base <= faixa["base_ate"]:
            imposto = (base * faixa["aliquota"]) - faixa["parcela_deduzir"]
            return max(imposto, 0.0)

    ultima = TABELA_IRPF_2026[-1]
    imposto = (base * ultima["aliquota"]) - ultima["parcela_deduzir"]
    return max(imposto, 0.0)