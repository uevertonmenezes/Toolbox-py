from descontos.descontos_previdenciarios import calcular_descontos_legais

from enum import Enum
from typing import TypedDict


class VerbasFerias(TypedDict):
    valor_proporcional: float
    terco_ferias: float
    abono: float
    terco_abono: float


class ResultadoFerias(TypedDict):
    valor_proporcional: float
    terco_ferias: float
    abono_pecuniario: float
    terco_abono_pecuniario: float
    adiantamento_parcela_decimo: float
    desconto_inss: float
    desconto_irpf: float
    valor_ferias: float


class AbonoPecuniario(str, Enum):
    sim = "sim"
    nao = "nao"


class AdiantarDecimo(str, Enum):
    sim = "sim"
    nao = "nao"


def calcular_verbas_ferias(
    salario_bruto: float,
    media_horas_extras: float,
    dias_ferias: int,
    abono_pecuniario: AbonoPecuniario,
) -> VerbasFerias:

    base_calculo = salario_bruto + media_horas_extras

    valor_proporcional = (base_calculo / 30) * dias_ferias
    terco_ferias = valor_proporcional / 3

    abono = 0.0
    terco_abono = 0.0

    if abono_pecuniario == AbonoPecuniario.sim:
        dias_abono = 10
        abono = (base_calculo / 30) * dias_abono
        terco_abono = abono / 3

    return {
        "valor_proporcional": valor_proporcional,
        "terco_ferias": terco_ferias,
        "abono": abono,
        "terco_abono": terco_abono,
    }


def calcular_ferias(
    salario_bruto: float,
    media_horas_extras: float,
    dias_ferias: int,
    abono_pecuniario: AbonoPecuniario,
    adiantar_decimo: AdiantarDecimo,
    dependentes: int = 0,
) -> ResultadoFerias:

    verbas = calcular_verbas_ferias(
        salario_bruto,
        media_horas_extras,
        dias_ferias,
        abono_pecuniario,
    )


    adiantamento_decimo = 0.0

    if adiantar_decimo == AdiantarDecimo.sim:
        adiantamento_decimo = salario_bruto / 2


    valor_bruto_ferias = (
        verbas["valor_proporcional"]
        + verbas["terco_ferias"]
        + verbas["abono"]
        + verbas["terco_abono"]
    )

    base_para_descontos = valor_bruto_ferias


    desconto_inss, desconto_irpf = calcular_descontos_legais(
        base_para_descontos,
        dependentes
    )


    valor_liquido = (
        valor_bruto_ferias
        - desconto_inss
        - desconto_irpf
        + adiantamento_decimo
    )

    return {
        "valor_proporcional": round(verbas["valor_proporcional"], 2),
        "terco_ferias": round(verbas["terco_ferias"], 2),
        "abono_pecuniario": round(verbas["abono"], 2),
        "terco_abono_pecuniario": round(verbas["terco_abono"], 2),
        "adiantamento_parcela_decimo": round(adiantamento_decimo, 2),
        "desconto_inss": round(desconto_inss, 2),
        "desconto_irpf": round(desconto_irpf, 2),
        "valor_ferias": round(valor_liquido, 2),
    }
