from plates import is_valid

def test_is_valid():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False
    assert is_valid("P13.14") == False
    assert is_valid("1234") == False
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False
    assert is_valid("HOLY!!") == False