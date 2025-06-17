from collections.abc import Iterable
import pytest

from src.utils import does_column_exist, has_csv_extension

class CustomReader:
    def __init__(self):
        self._values = (["brand", "cost", "reviews", "publication year"], ["", "", "", ""])

    def __iter__(self):
        return iter(self._values)

@pytest.fixture
def reader() -> Iterable:
    return CustomReader()

@pytest.mark.parametrize(("column", "res"),
    [
        ("brand", True),
        ("reviews", True),
        ("rating", False),
    ]
)
def test_does_exist_column(reader, column, res):
    assert does_column_exist(reader, column) == res

@pytest.mark.parametrize(("filename", "res"),
    [
        ("test_data.csv", True),
        ("test_data.txt", False),
        ("test.py", False),
        ("t.c", False),
    ]
)
def test_has_csv_extension(filename, res):
    assert has_csv_extension("tests/data/" + filename) == res
