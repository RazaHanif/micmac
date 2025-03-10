from twttr import shorten

def test_shorten():
    assert shorten("Hello, world") == "Hll, wrld"
    assert shorten("My name is Raza") == "My nm s Rz"
    assert shorten("Abc") == "bc"
    assert shorten("14 Fairlight") == "14 Frlght"
