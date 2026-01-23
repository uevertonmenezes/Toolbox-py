import pytest
from calculadora_horasExtras import calcular_horas_extras

def test_calculo_basico_horas_extras():
    resultado = calcular_horas_extras(
        salario_bruto=1621.0,
        hora_mes=220,
        hora_extra50="01:00",
        hora_extra100="01:00",
        hora_noturna="01:00"
    )

    assert resultado["valor_hora_trabalhada"] == 07.37
    assert resultado["total_hora_extra50"] == 11.05
    assert resultado["total_hora_extra100"] == 14.74
    assert resultado["total_hora_noturna"] == 13.26
    assert resultado["total_geral"] == 39.05

def test_formato_hora_invalido():
    with pytest.raises(ValueError):
        calcular_horas_extras(
            salario_bruto=2200,
            hora_mes=220,
            hora_extra50="2h",
            hora_extra100="01:00",
            hora_noturna="01:00"
        )

def test_sem_horas_extras():
    resultado = calcular_horas_extras(
        salario_bruto=3000,
        hora_mes=220,
        hora_extra50="00:00",
        hora_extra100="00:00",
        hora_noturna="00:00"
    )

    assert resultado["total_geral"] == 0

def test_estrutura_retorno():
    resultado = calcular_horas_extras(
        salario_bruto=2000,
        hora_mes=220,
        hora_extra50="01:00",
        hora_extra100="00:00",
        hora_noturna="00:00"
    )

    assert isinstance(resultado, dict)
    assert "total_geral" in resultado
