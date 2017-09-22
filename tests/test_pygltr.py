import pytest

from pygltr.pygltr import pretty_time


@pytest.mark.parametrize("seconds, result", [
    (60, '0h 1min'),
    (3600, '1h 0min'),
    (3720, '1h 2min'),
])
def test_pretty_time(seconds, result):
    assert pretty_time(seconds) == result
