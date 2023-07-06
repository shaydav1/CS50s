from fuel import convert, gauge
import pytest


def test_convert():
    assert convert("3/4") == 75


def test_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")


def test_value_error():
    with pytest.raises(ValueError):
        convert("three/four")


def test_gauge():
    assert gauge(75) == '75%'


def test_empty_gauge():
    assert gauge(1) == 'E'


def test_full_gauge():
    assert gauge(99) == 'F'
