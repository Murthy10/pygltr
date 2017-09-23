import pytest

from pygltr.pygltr import pretty_time, issue_to_row, sum_milestones


@pytest.mark.parametrize("seconds, result", [
    (60, '0h 1min'),
    (3600, '1h 0min'),
    (3720, '1h 2min'),
])
def test_pretty_time(seconds, result):
    assert pretty_time(seconds) == result


def test_issue_to_row(issues):
    rows = []
    for issue in issues:
        rows.append(issue_to_row(issue))
    assert len(rows) == 2


def test_sum_milestones(issues):
    rows = []
    for issue in issues:
        rows.append(issue_to_row(issue))
    milestones = sum_milestones(rows)
    assert milestones['Project_setup']['spent'] == 28800
