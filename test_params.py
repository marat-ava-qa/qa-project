import pytest

def is_expensive(price):
    return price > 1000

@pytest.mark.parametrize("price, expected",[
    (0, False),
    (999, False),
    (1000, False),
    (1001, True)
])

def test_is_expensive(price, expected):
    assert is_expensive(price) == expected