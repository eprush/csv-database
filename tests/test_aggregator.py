from contextlib import nullcontext as does_not_raise
import pytest

from src.command_handlers.aggregator import Aggregator


@pytest.fixture(scope="session")
def data():
    return {"rating": ["0.000", "-0.4", "1.0", "2", "2.1", "2.11", "-0.09"]}


@pytest.fixture(scope="session")
def column():
    return "rating"


@pytest.fixture(scope="session")
def sign():
    return "="


@pytest.mark.parametrize(("command", "expectation"),
    [
        ("rating=avg", does_not_raise()),
        ("rating=min", does_not_raise()),
        ("rating=max", does_not_raise()),
        ("rating>max", pytest.raises(ValueError)),
    ]
)
def test_parse_command(command: str, expectation):
    with expectation:
        print(*Aggregator(command).parse_command())


@pytest.mark.parametrize(("command", "res", "expectation"),
    [
        ("rating=avg", {"rating": [0.96]}, does_not_raise()),
        ("rating=min", {"rating": [-0.4]}, does_not_raise()),
        ("rating=max", {"rating": [2.11]}, does_not_raise()),
        ("rating=supermax", ..., pytest.raises(ValueError)),
    ]
)
def test_process(data, column, sign, command, res, expectation):
    agg = Aggregator(command)
    *_, param = agg.parse_command()
    with expectation:
        assert agg.process(data, column=column, sign=sign, param=param) == res
