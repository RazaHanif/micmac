from bank import value

def test_value_zero():
    assert value("Hello, world") == 0
    assert value("hello") == 0

def test_value_twenty():
    assert value("Hey") == 20
    assert value("howdy") == 20
    assert value("How are you?") == 20

def test_value_hundo():
    assert value("Welcome") == 100
    assert value("what's up") == 100