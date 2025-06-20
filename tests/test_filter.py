from contextlib import nullcontext as does_not_raise
import pytest

from src.command_handlers.filter import Filter
from tests.fixtures import data


@pytest.mark.parametrize(("command", "res", "expectation"),
    [
        ("rating=1", ("rating", "=", "1"), does_not_raise()),
        ("rating>0.0", ("rating", ">", "0.0"), does_not_raise()),
        ("rating<2,0", ("rating", "<", "2,0"), does_not_raise()),
        ("rating>=2", ..., pytest.raises(ValueError)),
    ]
)
def test_parse_command(command, res, expectation):
    with expectation:
        parsed = Filter(command).parse_command()
        assert parsed == res

equals_res = {
    "rating": ["1.0"],
    "brand": ["samsung"],
}

greater_res = {
    "rating": ["2.1", "2.11"],
    "brand": ["xiaomi", "lg"],
}

less_res = {
    "rating": ["-0.4", "-0.09"],
    "brand": ["siemens", "huawei"],
}
@pytest.mark.parametrize(("command", "res", "expectation"),
    [
        ("rating=1.0", equals_res, does_not_raise()),
        ("rating>2.0", greater_res, does_not_raise()),
        ("rating<0.0", less_res, does_not_raise()),
        ("rating=0,0", {"rating": [], "brand": []}, does_not_raise()),
        ("rating<0,0", ..., pytest.raises(TypeError)),
        ("rating>0,0", ..., pytest.raises(TypeError)),
        ("brand=1.0", ..., pytest.raises(TypeError)),
        ("brand>1.0", ..., pytest.raises(TypeError)),
        ("brand<1.0", ..., pytest.raises(TypeError)),
    ]
)
def test_process(data, command, res, expectation):
    f = Filter(command)
    column, sign, param = f.parse_command()
    with expectation:
        assert f.process(data, column=column, sign=sign, param=param) == res
