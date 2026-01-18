print('**Calculadora de Horas Extras**\n')

salario_bruto = float(input("Qual o seu salário bruto? (Sem os descontos)\n"))
hora_mes = float(input("Qual a sua carga horária mensal? (Considere 220h para uma jornada de 44h semanais)\n"))

hora_extra50 = (input("Qual a quantidade de horas extras normais trabalhadas? (Digite no formato HH:MM)\n"))
hora_extra100 = (input("Qual a quantidade de horas extras trabalhadas nos domingos e feriados (100%)? (Digite no formato HH:MM)\n"))
hora_noturna = (input("Qual a quantidade de horas noturnas trabalhadas? (Digite no formato HH:MM)\n"))

def converter_hora(hora):
    h, m = map(int, hora.split(':'))
    return h * 60 + m

min_extra50 = converter_hora(hora_extra50)
min_extra100 = converter_hora(hora_extra100)
min_noturna = converter_hora(hora_noturna)

valor_hora = salario_bruto / hora_mes
valor_minuto = valor_hora / 60

valor_extra50 = min_extra50 * valor_minuto * 1.5
valor_extra100 = min_extra100 * valor_minuto * 2
valor_noturna = (min_noturna * valor_minuto * 1.5) * 1.20

total = valor_extra50 + valor_extra100 + valor_noturna

print('\n**Resultado do Cálculo**\n')
print(f'Valor da hora trabalhada é: R${valor_hora:.2f}')
print(f'Valor da hora extra normal é: R${valor_extra50:.2f}')
print(f'Valor da hora extra 100% é: R${valor_extra100:.2f}')
print(f'Valor da hora noturna trabalhada é: R${valor_noturna:.2f}')
print(f'Valor total: R${total:.2f}')