import pytest
from fuel import convert
from fuel import gauge

def test_convert_correct():
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    assert convert("1/1") == 100
    assert convert("0/1") == 0

def test_convert_value():
    with pytest.raises(ValueError):
        convert("1!4")
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("5/2")

def test_convert_zero():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

def test_gauge():
    assert gauge(75) == "75%"
    assert gauge(25) == "25%"
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(-5) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(500) == "F"

def test_gauge_error():
    with pytest.raises(TypeError):
        assert gauge("1%") != "E"
        assert gauge(" ") != "%"
        assert gauge("99%") != "F"