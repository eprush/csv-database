from collections.abc import Iterable, Sized

from src.commands.abstract_command import AbstractCommandMaker, ProcessedData


def is_digital_column(column: Iterable | Sized) -> bool:
    """ Функция для проверки, что колонка содержит только числовые значения. """
    if len(column) == 0:
        raise ValueError("Column is empty")

    for value in column:
        try:
            float(value)
        except TypeError:
            return False
    return True


class Aggregator(AbstractCommandMaker):
    name: str | None = "aggregation"

    def validate(self) -> tuple[str, str, str]:
        parsed_command = [element for element in self._command.split("=") if len(element)]
        if len(parsed_command) != 2:
            raise ValueError(f"Invalid value for aggregation command: {self._command}")

        column, param = parsed_command
        return column, "=", param

    def make(self, previous_data: ProcessedData, *, column: str, sign:str, param: str) -> ProcessedData:
        values = previous_data[column]
        if not is_digital_column(values):
            raise ValueError(f"Aggregation column must be digital: {column=}")

        values = [float(v) for v in values]
        match param:
            case "min":
                return {column: [min(values)]}
            case "max":
                return {column: [max(values)]}
            case "avg":
                average = sum(values) / len(values)
                return {column: [average]}
            case _:
                raise ValueError(f"Invalid aggregation parameter: {param=}")

if __name__ == "__main__":
    print(is_digital_column(['0', '1', '2']))