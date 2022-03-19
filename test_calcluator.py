"""
Test suit for string_calculator.py
"""
from string_calculator import string_calculator

def test_string_calculator():
    assert string_calculator("") == 0
    assert string_calculator("2") == 2
    assert string_calculator("1,2") == 3


