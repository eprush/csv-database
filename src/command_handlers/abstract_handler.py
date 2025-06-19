from abc import ABC, abstractmethod
from collections.abc import Iterable

ProcessedData = dict[str, list[str] | Iterable[str]]

class AbstractCommandHandler(ABC):
    """ Интерфейс для обработчиков команд. """

    name: str | None = None

    def __init__(self, command: str):
        self._command = command

    @abstractmethod
    def parse_command(self) -> tuple[str, str, str]:
        """ Метод для получения названия колонки, знака оператора и параметра из строки команды. """
        ...

    @abstractmethod
    def process(self, previous_data: ProcessedData, *, column: str, sign:str, param: str) -> ProcessedData:
        """ Метод для выполнения команды. """
        ...
