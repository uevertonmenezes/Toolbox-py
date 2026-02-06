from descontos.inss import calcular_inss
from enum import Enum


class ParcelaDecimo(str, Enum):
    unica = "unica"
    primeira = "primeira"
    segunda = "segunda"

def calcular_decimo_terceiro(
        salario_bruto: float,
        meses_trabalhados: int,
        parcela: ParcelaDecimo
) -> dict:


    PARCELAS_VALIDAS = {"unica", "primeira", "segunda"}

    if parcela not in PARCELAS_VALIDAS:
        raise ValueError("Parcela inválida. Use: 'unica', 'primeira' ou 'segunda'")

    if salario_bruto <= 0:
        raise ValueError("Salário deve ser maior que zero")

    if not 0 <= meses_trabalhados <= 12:
        raise ValueError("Meses trabalhados deve estar entre 0 e 12")


    salario_mes = salario_bruto / 12
    base_calculo = salario_mes * meses_trabalhados

    if parcela == ParcelaDecimo.unica:
        desconto_inss = calcular_inss(base_calculo)
        decimo_terceiro = base_calculo - desconto_inss

    elif parcela == ParcelaDecimo.primeira:
        decimo_terceiro = base_calculo / 2

    elif parcela == ParcelaDecimo.segunda:
        metade = base_calculo / 2
        desconto_inss = calcular_inss(metade)
        decimo_terceiro = metade - desconto_inss

    return {
        "valor_decimo_terceiro": round(decimo_terceiro, 2)
    }
