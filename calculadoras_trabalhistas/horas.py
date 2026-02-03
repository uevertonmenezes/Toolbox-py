def calcular_horarios():
    print('**Calculadora de Horários (h:m)**')

    horario1 = input('Digite o primeiro horário (ex: 07:58)')
    horario2 = input('Digite o segundo horário (ex: 11:02)')

    try:
        h1, m1 = map(int, horario1.split(':'))
        h2, m2 = map(int, horario2.split(':'))

    except ValueError:
        print('\nErro: Formato inválido. Utilize ":" ao preencher o seu horário.')
        return

    minutos_inicial = (h1 * 60) + m1
    minutos_final = (h2 * 60) + m2

    minutos_diferença = minutos_final - minutos_inicial

    if minutos_diferença < 0:
        print('\nErro: O horário final é menor que o horário inicial.')

    horas_finais = minutos_diferença // 60

    minutos_finais = minutos_diferença % 60

    resultado_formatado = f"{horas_finais:02d}:{minutos_finais:02d}"

    print("-" * 30)
    print(f"O resultado é: {resultado_formatado}")
    print("-" * 30)

calcular_horarios()