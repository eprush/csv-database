from typing import Iterable

from src.commands.abstract_command import AbstractCommandMaker

class Filter(AbstractCommandMaker):
    def validate(self) -> tuple[str, str]:
        ...

    def make(self, previous_data: Iterable) -> Iterable:
        ...