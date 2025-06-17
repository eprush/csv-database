from collections.abc import Iterable
import pytest

from src.utils import does_exist_column, file_does_exist_and_has_csv

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
    assert does_exist_column(reader, column) == res

@pytest.mark.parametrize(("filename", "res"),
    [
        ("test_data.csv", True),
        ("test_data.txt", False),
        ("bullshit_for_test.py", False),
    ]
)
def test_file_does_exist_and_has_csv(filename, res):
    assert file_does_exist_and_has_csv("tests/data/" + filename) == res
