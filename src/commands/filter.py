from src.commands.abstract_command import AbstractCommandMaker, ProcessedData


class Filter(AbstractCommandMaker):
    name: str | None = ("filtration"
                        "")
    def validate(self) -> tuple[str, str, str]:
        ...

    def make(self, previous_data: ProcessedData, *, column: str, sign:str, param: str) -> ProcessedData:
        ...