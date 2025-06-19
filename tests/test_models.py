from dataclasses import FrozenInstanceError

import pytest

from src.models import CmdArgs

@pytest.fixture(scope="session")
def args():
    return CmdArgs("test_file")

def test_cannot_update_cmd_args(args):
    with pytest.raises(FrozenInstanceError):
        args.file = "another_test_file"
    with pytest.raises(FrozenInstanceError):
        args.where = "test_where"
    with pytest.raises(FrozenInstanceError):
        args.aggregate = "test_aggregate"
