from src.command_handlers.abstract_handler import AbstractCommandHandler, ProcessedData
from src.utils import is_digital_column


class Filter(AbstractCommandHandler):
    """ Обработчик команды фильтрации. """

    name: str | None = "filtration"

    def parse_command(self) -> tuple[str, str, str]:
        available_signs: tuple[str, ...] = ("=", ">", "<")
        parsed_command = tuple()
        result_sign = ""
        # Распарсим строку команды и сохраним знак (=/>/<)
        for sign in available_signs:
            if sign in self._command:
                parsed_command = tuple(element for element in self._command.split(sign) if len(element))
                result_sign = sign

        # Проверим, что
        # 1) после парсинга команда содержит только колонку и параметр
        # 2) не остались ли другие знаки (например, случай команды column>=param)
        if len(parsed_command) != 2 and any((s in c) for c in parsed_command for s in available_signs):
            raise ValueError(f"Invalid {self.name} command: {self._command}")
        column, param = parsed_command
        return column, result_sign, param

    def process(self, previous_data: ProcessedData, *, column: str, sign: str, param: str) -> ProcessedData:
        values = previous_data[column]
        match sign:
            case "=":
                filtered_indexes = [
                    idx for idx, value in enumerate(values)
                    if value == param
                ]
            case ">":
                if not is_digital_column(values):
                    raise TypeError(f"Filtration {column=} must be digital because of using {sign=}")
                filtered_indexes = [
                    idx for idx, value in enumerate(values)
                    if float(value) > float(param)
                ]
            case "<":
                if not is_digital_column(values):
                    raise TypeError(f"Filtration {column=} must be digital because of using {sign=}")
                filtered_indexes = [
                    idx for idx, value in enumerate(values)
                    if float(value) < float(param)
                ]
            case _:
                # Все проверки уже были сделаны.
                # Значит возникла непродуманная ошибка.
                raise Exception(f"Something went wrong with {self.name} command: {column=}, {sign=}, {param=}")

        for col in previous_data.keys():
            previous_data[col] = [
                item for idx, item in enumerate(previous_data[col])
                if idx in filtered_indexes
            ]
        return previous_data
