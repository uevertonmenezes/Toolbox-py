import pytest
from calculadoras_trabalhistas.horas import calcular_total

@pytest.mark.parametrize(
    "intervalos, esperado",
    [
        (
            [("07:00", "11:05")],
            "04:05"
        ),

        (
            [("07:00", "11:05"), ("13:00", "17:05")],
            "08:10"
        ),

        (
            [("07:00", "11:05"), ("13:00", "17:05"), ("18:00", "20:00")],
            "10:10"
        ),

        (
            [
                ("07:00", "11:05"),
                ("13:00", "17:05"),
                ("18:00", "20:00"),
                ("22:00", "23:00"),
            ],
            "11:10"
        ),

        (
            [
                ("08:00", "09:00"),
                ("09:30", "10:30"),
                ("11:00", "12:00"),
                ("13:00", "14:00"),
                ("15:00", "16:00"),
            ],
            "05:00"
        ),
    ]
)
def test_calcular_total(intervalos, esperado):
    assert calcular_total(intervalos) == esperado


def test_horario_final_menor():
    with pytest.raises(ValueError):
        calcular_total([("18:00", "08:00")])


def test_formato_invalido():
    with pytest.raises(ValueError):
        calcular_total([("8h", "12:00")])
