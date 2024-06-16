from seasons import get_diff
from datetime import datetime


def test_seasons():
    start_date = datetime.strptime("1999-01-01", "%Y-%m-%d").date()
    end_date = datetime.strptime("2000-01-01", "%Y-%m-%d").date()
    assert get_diff(start_date, end_date) == 365


def test_seasons2():
    start_date = datetime.strptime("2020-06-01", "%Y-%m-%d").date()
    end_date = datetime.strptime('2032-01-01', "%Y-%m-%d").date()
    assert get_diff(start_date, end_date) == 4231
