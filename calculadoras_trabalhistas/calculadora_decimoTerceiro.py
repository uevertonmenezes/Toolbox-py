print("**Calculadora de décimo terceiro**")

salario_bruto = float(input("Qual o seu salário bruto?"))

meses_trabalhados = int(input("Quantos meses você trabalhou esse ano?"))

salario_mes = salario_bruto / 12
decimo_terceiro = salario_mes * meses_trabalhados

print('o valor do seu décimo terceiro é de', decimo_terceiro)