print('**Calculadora de Horas Extras**')

salario_bruto = float(input("Qual o seu salário bruto?"))

hora_normal = salario_bruto / 220
hora_extra = hora_normal / 0.5

print('O seu valor por cada hora extra é de', hora_extra)