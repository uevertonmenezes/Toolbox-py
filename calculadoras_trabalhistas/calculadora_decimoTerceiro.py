print("**Calculadora de Décimo Terceiro**")

salario_bruto = float(input("Qual o seu salário bruto? (Sem os descontos)\n"))
meses_trabalhados = int(input("Quantos meses você trabalhou esse ano?\n"))
parcela_decimo = float(input(
    "Qual parcela deseja simular?\n"
        "0- Única\n"
        "1- Primeira Parcela\n"
        "2- Segunda Parcela\n"))

salario_mes = salario_bruto / 12

if parcela_decimo == 0:
    decimo_terceiro = (salario_mes * meses_trabalhados) * (91 / 100) #alíquota de teste (9%), logo mais será adicionado tabela real de alíquotas

elif parcela_decimo == 1:
    decimo_terceiro = (salario_mes * meses_trabalhados) / 2

else:
    decimo_terceiro = (salario_mes * meses_trabalhados) / 2 * (91 / 100)

print(f'o valor do seu décimo terceiro é de: R${decimo_terceiro:.2f}')
