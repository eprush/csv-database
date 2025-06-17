from collections.abc import Sequence
from contextlib import nullcontext as does_not_raise
import pytest
from typing import Any

from src.aggregator import is_digital_column, raise_if_incorrect_aggregation

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

@pytest.mark.parametrize(("param", "expectation"),
    [
        ("avg", does_not_raise()),
        ("min", does_not_raise()),
        ("max", does_not_raise()),
        ("desc", pytest.raises(ValueError)),
        (1, pytest.raises(ValueError)),
    ]
)
def test_raise_if_incorrect_aggregation(param: Any, expectation):
    with expectation:
        raise_if_incorrect_aggregation(param)
