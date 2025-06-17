from collections.abc import Iterable, Sized
from src.commands.abstract_command import AbstractCommandMaker


def is_digital_column(column: Iterable | Sized) -> bool:
    """ Функция для проверки, что колонка содержит только числовые значения. """
    if len(column) == 0:
        raise ValueError("Column is empty")

    for value in column:
        if type(value) not in (int, float):
            return False
    return True


class Aggregator(AbstractCommandMaker):
    def validate(self) -> tuple[str, str]:
        parsed_command = [element for element in self._command.split("=") if len(element)]
        if len(parsed_command) != 2:
            raise ValueError(f"Invalid value for aggregation command: {self._command}")

        column, aggregation_param = parsed_command

        if aggregation_param not in ("avg", "min", "max"):
            raise ValueError(f"Invalid aggregation parameter: {aggregation_param}")

        return column, aggregation_param

    def make(self, previous_data: Iterable) -> Iterable:
        ...
        return []
