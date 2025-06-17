from dataclasses import dataclass

@dataclass(frozen=True)
class CmdArgs:
    file: str
    where: str | None = None
    aggregate: str | None = None
