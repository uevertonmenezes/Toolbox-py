import pytest
from calculadoras_trabalhistas.decimo_terceiro import calcular_decimo_terceiro, ParcelaDecimo


def test_primeira_parcela_sem_desconto():
    resultado = calcular_decimo_terceiro(
        salario_bruto=3000.00,
        meses_trabalhados=12,
        parcela=ParcelaDecimo.primeira
    )

    assert resultado["valor_bruto"] == 1500.00
    assert resultado["desconto_inss"] == 0.0
    assert resultado["desconto_irpf"] == 0.0
    assert resultado["valor_decimo_terceiro"] == 1500.00


def test_segunda_parcela_com_desconto():
    resultado = calcular_decimo_terceiro(
        salario_bruto=3000.00,
        meses_trabalhados=12,
        parcela=ParcelaDecimo.segunda
    )

    assert resultado["valor_bruto"] == 1500.00
    assert resultado["desconto_inss"] > 0
    assert resultado["desconto_irpf"] >= 0
    assert resultado["valor_decimo_terceiro"] < 1500.00


def test_parcela_unica_com_desconto():
    resultado = calcular_decimo_terceiro(
        salario_bruto=3000.00,
        meses_trabalhados=12,
        parcela=ParcelaDecimo.unica
    )

    assert resultado["valor_bruto"] == 3000.00
    assert resultado["desconto_inss"] > 0
    assert resultado["desconto_irpf"] >= 0
    assert resultado["valor_decimo_terceiro"] < 3000.00


def test_dependentes_reduzem_irpf_quando_ha_imposto():
    sem_dependentes = calcular_decimo_terceiro(
        salario_bruto=7000.00,
        meses_trabalhados=12,
        parcela=ParcelaDecimo.unica,
        dependentes=0
    )

    com_dependentes = calcular_decimo_terceiro(
        salario_bruto=7000.00,
        meses_trabalhados=12,
        parcela=ParcelaDecimo.unica,
        dependentes=1
    )

    assert sem_dependentes["desconto_irpf"] > 0
    assert com_dependentes["desconto_irpf"] < sem_dependentes["desconto_irpf"]


def test_dependentes_nao_afetam_irpf_quando_isento():
    sem_dependentes = calcular_decimo_terceiro(
        salario_bruto=4000.00,
        meses_trabalhados=12,
        parcela=ParcelaDecimo.unica,
        dependentes=0
    )

    com_dependentes = calcular_decimo_terceiro(
        salario_bruto=4000.00,
        meses_trabalhados=12,
        parcela=ParcelaDecimo.unica,
        dependentes=2
    )
    assert sem_dependentes["desconto_irpf"] == 0.0
    assert com_dependentes["desconto_irpf"] == 0.0


def test_decimo_terceiro_zero_meses():
    resultado = calcular_decimo_terceiro(
        salario_bruto=4000.00,
        meses_trabalhados=0,
        parcela=ParcelaDecimo.unica
    )

    assert resultado["valor_decimo_terceiro"] == 0.0


def test_parcela_invalida():
    with pytest.raises(ValueError):
        calcular_decimo_terceiro(3000, 12, "terceira")


def test_salario_invalido():
    with pytest.raises(ValueError):
        calcular_decimo_terceiro(0, 12, ParcelaDecimo.unica)


def test_meses_invalidos():
    with pytest.raises(ValueError):
        calcular_decimo_terceiro(3000, 13, ParcelaDecimo.unica)
