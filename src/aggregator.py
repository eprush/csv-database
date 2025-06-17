from collections.abc import Iterable, Sized
from typing import Literal


def is_digital_column(column: Iterable | Sized) -> bool:
    """ Функция для проверки, что колонка содержит только числовые значения. """
    if len(column) == 0:
        raise ValueError("Column is empty")

    for value in column:
        if type(value) not in (int, float):
            return False
    return True

def raise_if_incorrect_aggregation(parameter: Literal["avg", "min", "max"]):
    if parameter not in ("avg", "min", "max"):
        raise ValueError(f"Invalid aggregation with {parameter=}")
