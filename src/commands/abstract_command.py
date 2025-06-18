from abc import ABC, abstractmethod
from collections.abc import Iterable

ProcessedData = dict[str, list | Iterable]

class AbstractCommandMaker(ABC):
    name: str | None = None

    def __init__(self, command: str):
        self._command = command

    @abstractmethod
    def validate(self) -> tuple[str, str, str]:
        ...

    @abstractmethod
    def make(self, previous_data: ProcessedData, *, column: str, sign:str, param: str) -> ProcessedData:
        ...
