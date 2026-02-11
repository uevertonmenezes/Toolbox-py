def calcular_intervalo(horario_inicial: str, horario_final: str) -> int:
    try:
        h1, m1 = map(int, horario_inicial.split(":"))
        h2, m2 = map(int, horario_final.split(":"))
    except ValueError:
        raise ValueError("Formato inválido. Use HH:MM")

    inicio =h1 * 60 +m1
    final = h2 * 60 + m2

    if final < inicio:
        raise ValueError("Horário final menor que o inicial")

    return final - inicio


def calcular_total(intervalos: list[tuple[str, str]]) -> str:
    total_minutos = 0

    for inicio, final in intervalos:
        total_minutos += calcular_intervalo(inicio, final)

    horas = total_minutos // 60
    minutos = total_minutos % 60

    return f"{horas:02d}:{minutos:02d}"