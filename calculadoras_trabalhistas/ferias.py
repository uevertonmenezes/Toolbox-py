
print('**Calculadora de Férias**')

salario_bruto = float(input("Qual o seu salário bruto?"))
ferias_bruto = salario_bruto + (salario_bruto / 3)
valor_descontado = ferias_bruto * (9 / 100) #definir alíquotas e descontos

remuneracao_ferias = ferias_bruto - valor_descontado
print("O total a receber das suas férias é", remuneracao_ferias)
