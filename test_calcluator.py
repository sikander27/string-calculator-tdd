"""
Test suit for add.py
"""
import pytest
from string_calculator import add

def test_add():
    # Basic test with empty string, single number string and 2 comma separted stireng
    assert add("") == 0
    assert add("2") == 2
    assert add("1,2") == 3

    # test for multiple comma separated numbers
    assert add("1, 2, 3") == 6

    # Allow the Add method to handle new lines between numbers (instead of commas).
    assert add("1\n2,3") == 6
    assert add("1,\n, 2") == 3

    # Support different delimiters
    assert add("//;\n1;2") == 3

    # For negative number it should throw an exception "negatives not allowed" with the number.

    with pytest.raises(Exception, match = r'negatives not allowed [-1, -2]'):
        add("2, -1, -2")

