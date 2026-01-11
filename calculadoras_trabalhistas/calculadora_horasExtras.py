print('**Calculadora de Horas Extras**\n')

salario_bruto = float(input("Qual o seu salário bruto? (Sem os descontos)\n"))
hora_mes = float(input("Qual a sua carga horária mensal? (Considere 220h para uma jornada de 44h semanais)\n"))
porcentagem_hora = float(input("Qual a porcentagem da hora? (Considere 50% para dias comuns e 100% para domingos e feriados)\n"))
horas_trabalhadas = float(input("Qual a quantidade de horas extras trabalhadas?\n"))

hora_normal = salario_bruto / hora_mes

if porcentagem_hora == 50:
    hora_extra = hora_normal + (hora_normal * 0.5)
else:
    hora_extra = hora_normal + (hora_normal * 1)

hora_total = hora_extra * horas_trabalhadas

print(f'Valor da hora normal é: R${hora_normal:.2f}')
print(f'O valor por cada hora extra é de: R${hora_extra:.2f}')
print(f'O valor total pelas horas extras trabalhadas é de: R${hora_total:.2f}')