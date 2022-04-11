"""
Test suit for string_calculator.py
"""
import pytest
from string_calculator import add, add_2

def test_empty_string():
    # Basic test with empty string
    assert add("") == 0

def test_single_number_string():
    # test with single number string 
    assert add("2") == 2

def test_string_with_two_numbers():
    # test with valid input (two comma separted numbers)
    assert add("1,2") == 3

def test_string_with_multiple_numbers():
    # test for multiple comma separated numbers
    assert add("1, 2, 3") == 6

def test_string_new_line():
    # Allow the Add method to handle new lines between numbers (instead of commas).
    assert add("1\n2,3") == 6
    assert add("1,\n, 2") == 3

def test_string_different_delimeters():
    # Support different delimiters
    assert add("//;\n1;2") == 3
    assert add('//[***][%]&\n1***2***3&5|1{}3') == 15

def test_string_with_negative_number():
    # For negative number it should throw an exception "negatives not allowed" with the number.
    with pytest.raises(Exception, match = r'negatives not allowed \[-1, -2\]'):
        add("2, -1, -2")

def test_string_with_alphabets():
    # test string with no numbers only string. It should return 0
    assert add("a, b") == 0

def test_number_with_underscore():

    assert add("1_000, 2_000") == 3000

def test_odd_even_index_scenario():

    assert add_2("1,3,4,7,6") == 1
    assert add_2("1,2") == -1
    assert add_2("") == 0
    assert add_2("2") == 2
    assert add_2("1\n2,3") == 2
    assert add_2("1,\n, 2") == -1
    assert add_2('//[***][%]&\n1***2***3&5|1{}3') == -5
    assert add_2("1_000, 2_000") == -1000


















