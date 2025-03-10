import pytest
from datetime import date
from seasons import difference
from seasons import get_date


def test_difference():
    assert difference(date(2023, 1, 1), date(2022, 1, 1)) == 525600
    with pytest.raises(UnboundLocalError):
        difference(2023, 2025)
        difference(date(2023, 1, 1), date(2025, 1, 1))


def test_get_date():
    assert get_date("2023-01-01") == date(2023, 1, 1)
    with pytest.raises(SystemExit):
        get_date("march, 12 1997")
