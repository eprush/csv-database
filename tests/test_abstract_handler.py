import pytest

from src.command_handlers.abstract_handler import AbstractCommandHandler

def test_cannot_create_abstract_command_handler():
    with pytest.raises(TypeError):
        AbstractCommandHandler(...)


def test_can_create_subclass():
    class Test(AbstractCommandHandler):
        def parse_command(self) -> tuple[str, str, str]: pass

        def process(self, previous_data, *, column: str, sign: str, param: str): pass

    t = Test(...)
    assert isinstance(t, AbstractCommandHandler)
