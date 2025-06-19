from src.command_handlers.abstract_handler import AbstractCommandHandler, ProcessedData
from src.utils import is_digital_column


class Aggregator(AbstractCommandHandler):
    """ Обработчик команды агрегации. """

    name: str | None = "aggregation"

    def parse_command(self) -> tuple[str, str, str]:
        parsed_command = [element for element in self._command.split("=") if len(element)]

        # Проверим, что после парсинга команда содержит только колонку и параметр
        if len(parsed_command) != 2:
            raise ValueError(f"Invalid value for {self.name} command: {self._command}")
        column, param = parsed_command
        return column, "=", param

    def process(self, previous_data: ProcessedData, *, column: str, sign:str, param: str) -> ProcessedData:
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
                # Случай неподходящего параметра агрегации
                raise ValueError(f"Invalid aggregation parameter: {param=}")
