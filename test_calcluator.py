"""
Test suit for add.py
"""
from string_calculator import add

def test_add():
    # Basic test with empty string, single number string and 2 comma separted stireng
    assert add("") == 0
    assert add("2") == 2
    assert add("1,2") == 3

    # test for multiple comma separated numbers
    assert add("1, 2, 3") == 6




