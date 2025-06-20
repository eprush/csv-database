from collections.abc import Iterable, Sequence
from contextlib import nullcontext as does_not_raise

import pytest

from src.utils import does_column_exist, has_csv_extension, is_digital_column


class CustomHeaders:
    def __init__(self):
        self._values = ["brand", "cost"]

    def __iter__(self):
        return iter(self._values)


@pytest.fixture
def headers() -> Iterable:
    return CustomHeaders()


@pytest.mark.parametrize(("column", "res"),
    [
        ("brand", True),
        ("rating", False),
    ]
)
def test_does_exist_column(headers, column, res):
    assert does_column_exist(column, headers=headers) == res


@pytest.mark.parametrize(("filename", "res"),
    [
        ("test_data.csv", True),
        ("test_data.txt", False),
        ("t.c", False),
    ]
)
def test_has_csv_extension(filename, res):
    assert has_csv_extension("tests/data/" + filename) == res


@pytest.mark.parametrize(("values", "res", "expectation"),
    [
        ([0,"-0.1"], True, does_not_raise()),
        ([1, "1", 3], True, does_not_raise()),
        (["0,1"], False, does_not_raise()),
        (["test", 1, 1, 1], False, does_not_raise()),
        ([], ..., pytest.raises(ValueError)),
    ]
)
def test_is_digital_column(values: Sequence, res, expectation):
    with expectation:
        assert is_digital_column(values) == res

