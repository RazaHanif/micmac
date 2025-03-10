import pytest
from um import count


def test_zero():
    assert count("Hello, world") == 0
    assert count("umbrella") == 0



def test_one():
    assert count("um") == 1
    assert count("UM") == 1
    assert count("Hello um, world") == 1


def test_two():
    assert count("Hello um, world, I um...... how are you") == 2


def test_multiple():
    assert count("um, um... um not bum") == 3
