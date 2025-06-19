from dataclasses import dataclass


@dataclass(frozen=True)
class CmdArgs:
    """ Модель данных аргументов командной строки. """
    file: str
    where: str | None = None
    aggregate: str | None = None
