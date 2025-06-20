import pytest
from contextlib import nullcontext as does_not_raise

from src.main import _get_data_from_file

csv_res = {
    "brand": ["0"],
    "cost": ["0"],
    "reviews": ["0"],
    "publication year": ["0"]
}

@pytest.mark.parametrize(("filename", "res", "expectation"),
    [
        ("tests/data/test_data.csv", csv_res, does_not_raise()),
        ("tests/data/test_data.txt", ..., pytest.raises(ValueError)),
        ("tests/data/another_test_data.csv", ..., pytest.raises(FileNotFoundError)),
    ]
)
def test_get_data_from_file(filename, res, expectation):
    with expectation:
        assert _get_data_from_file(filename) == res
