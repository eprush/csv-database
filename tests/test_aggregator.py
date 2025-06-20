from contextlib import nullcontext as does_not_raise
import pytest

from src.command_handlers.aggregator import Aggregator
from tests.fixtures import data


@pytest.mark.parametrize(("command", "res","expectation"),
    [
        ("rating=avg", ("rating", "=", "avg"), does_not_raise()),
        ("rating=min", ("rating", "=", "min"), does_not_raise()),
        ("rating=max", ("rating", "=", "max"), does_not_raise()),
        ("rating=supermax", ("rating", "=", "supermax"), does_not_raise()),
        ("brand=avg", ("brand", "=", "avg"), does_not_raise()),
        ("rating>max", ..., pytest.raises(ValueError)),
    ]
)
def test_parse_command(command: str, res, expectation):
    with expectation:
        parsed = Aggregator(command).parse_command()
        assert parsed == res


@pytest.mark.parametrize(("command", "res", "expectation"),
    [
        ("rating=avg", {"avg": [0.96]}, does_not_raise()),
        ("rating=min", {"min": [-0.4]}, does_not_raise()),
        ("rating=max", {"max": [2.11]}, does_not_raise()),
        ("rating=supermax", ..., pytest.raises(ValueError)),
        ("brand=avg", ..., pytest.raises(TypeError)),
    ]
)
def test_process(data, command, res, expectation):
    agg = Aggregator(command)
    column, sign, param = agg.parse_command()
    with expectation:
        assert agg.process(data, column=column, sign=sign, param=param) == res
