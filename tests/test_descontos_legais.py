from calculadoras_trabalhistas.decimo_terceiro import calcular_descontos_legais


def test_calcular_descontos_legais_retorna_inss_irpf():
    desconto_inss, desconto_irpf = calcular_descontos_legais(
        valor_bruto=7000.00,
        dependentes=0
    )

    assert desconto_inss > 0
    assert desconto_irpf > 0


def test_dependentes_reduzem_irpf():
    _, irpf_sem = calcular_descontos_legais(
        valor_bruto=7000.00,
        dependentes=0
    )

    _, irpf_com = calcular_descontos_legais(
        valor_bruto=7000.00,
        dependentes=1
    )

    assert irpf_com < irpf_sem


def test_irpf_zerado_ate_5000():
    _, descontos_irpf = calcular_descontos_legais(
        valor_bruto=5000.00,
        dependentes=0
    )

    assert descontos_irpf == 0.0


def test_calcular_descontos_legais_irpf_zerado_e_inss_aplicado():
    desconto_inss, desconto_irpf = calcular_descontos_legais(
        valor_bruto=2000.00,
        dependentes=0
    )

    assert desconto_inss > 0
    assert desconto_irpf == 0.0
