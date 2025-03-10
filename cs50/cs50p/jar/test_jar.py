import pytest
from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar_two = Jar(15)
    assert jar_two.capacity == 15


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    with pytest.raises(ValueError):
        jar.deposit(15)


def test_withdraw():
    jar = Jar()
    jar.deposit(8)
    jar.withdraw(5)
    assert str(jar) == "🍪🍪🍪"
    with pytest.raises(ValueError):
        jar.withdraw(5)
