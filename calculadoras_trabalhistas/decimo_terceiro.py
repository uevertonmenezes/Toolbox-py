from descontos.descontos_previdenciarios import calcular_descontos_legais

from enum import Enum
from typing import TypedDict


class ResultadoDecimoTerceiro(TypedDict):
    parcela: str
    valor_bruto: float
    desconto_inss: float
    desconto_irpf: float
    valor_decimo_terceiro: float


class ParcelaDecimo(str, Enum):
    unica = "unica"
    primeira = "primeira"
    segunda = "segunda"


def calcular_decimo_terceiro(
        salario_bruto: float,
        meses_trabalhados: int,
        parcela: ParcelaDecimo,
        dependentes: int = 0
) -> ResultadoDecimoTerceiro:

    if not isinstance(parcela, ParcelaDecimo):
        raise ValueError("Parcela inválida")

    elif salario_bruto <= 0:
        raise ValueError("Salário deve ser maior que zero")

    elif not 0 <= meses_trabalhados <= 12:
        raise ValueError("Meses trabalhados deve estar entre 0 e 12")

    salario_mes = salario_bruto / 12
    base_calculo = salario_mes * meses_trabalhados

    valor_bruto = 0.0
    desconto_inss = 0.0
    desconto_irpf = 0.0

    if parcela == ParcelaDecimo.primeira:
        valor_bruto = base_calculo / 2

    elif parcela == ParcelaDecimo.segunda:
        valor_bruto = base_calculo / 2
        desconto_inss, desconto_irpf = calcular_descontos_legais(
            valor_bruto, dependentes
        )

    elif parcela == ParcelaDecimo.unica:
        valor_bruto = base_calculo
        desconto_inss, desconto_irpf = calcular_descontos_legais(
            valor_bruto, dependentes
        )

    valor_liquido = valor_bruto - desconto_inss - desconto_irpf

    return {
        "parcela": str(parcela.value),
        "valor_bruto": round(valor_bruto, 2),
        "desconto_inss": round(desconto_inss, 2),
        "desconto_irpf": round(desconto_irpf, 2),
        "valor_decimo_terceiro": round(valor_liquido, 2)
    }