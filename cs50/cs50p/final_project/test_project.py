import pytest
from project import get_amount, symbol, currency

# test the amount function make sure bad inputs dont fail
def test_get_amount(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 5)
    result = get_amount()
    assert result == 5

    monkeypatch.setattr('builtins.input', lambda _: 15)
    result = get_amount()
    assert result == 15

# test the symbol function make sure the correct symbol is returned
def test_symbol():
    assert symbol("cad") == "$"
    assert symbol("gbp") == "£"
    assert symbol("jpy") == "¥"


# test the currency function make sure bad inputs dont fail
def test_currency(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "cad")
    result = currency("starting")
    assert result == "cad"
