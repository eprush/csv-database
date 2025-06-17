from abc import ABC, abstractmethod
from collections.abc import Iterable


class AbstractCommandMaker(ABC):
    def __init__(self, command: str):
        self._command = command

    @abstractmethod
    def validate(self) -> tuple[str, str]:
        ...

    @abstractmethod
    def make(self, previous_data: Iterable) -> Iterable:
        ...
