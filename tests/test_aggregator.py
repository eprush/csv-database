from collections.abc import Sequence
from contextlib import nullcontext as does_not_raise
import pytest

from src.commands.aggregator import Aggregator, is_digital_column

@pytest.mark.parametrize(("values", "res", "expectation"),
    [
        ([1,2,3], True, does_not_raise()),
        ([-1,0,1,-1.1], True, does_not_raise()),
        ([0, "1", 3], False, does_not_raise()),
        ([], False, pytest.raises(ValueError)),
    ]
)
def test_is_digital_column(values: Sequence, res, expectation):
    with expectation:
        assert is_digital_column(values) == res

@pytest.mark.parametrize(("command", "expectation"),
    [
        ("rating=avg", does_not_raise()),
        ("rating=min", does_not_raise()),
        ("rating=max", does_not_raise()),
        ("rating>max", pytest.raises(ValueError)),
    ]
)
def test_validate(command: str, expectation):
    with expectation:
        print(*Aggregator(command).validate())
