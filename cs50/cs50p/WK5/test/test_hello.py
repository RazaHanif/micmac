from hello import hello

def test_default():
    assert hello() == "Hello, world"

def test_args():
    assert hello("David") == "Hello, David"