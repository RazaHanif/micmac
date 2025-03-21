import pytest
from numb3rs import validate


def test_true():
    assert validate("127.0.0.1") == True
    assert validate("1.2.3.4") == True
    assert validate("255.255.255.255") == True
    assert validate("168.0.0.1") == True


def test_false():
    assert validate("1.2.3.1000") == False
    assert validate("512.512.512.512") == False
    assert validate("255.257.258.260") == False
    assert validate("1.2.3.4.5") == False
    assert validate("cat") == False
