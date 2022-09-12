import pytest


@pytest.mark.parametrize(
    'a, b, expected_result', (
            (1,1,2),
            (1, 2, 3),
    )
)
def test__ls_report(a,b,expected_result):
    assert a+b==expected_result