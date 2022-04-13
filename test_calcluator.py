"""
Test suit for string_calculator.py
"""
import pytest
import string_calculator
from test_base import set_keyboard_input, get_display_output
def test_empty_string():
    # Basic test with empty string
    assert string_calculator.add("") == 0

def test_single_number_string():
    # test with single number string 
    assert string_calculator.add("2") == 2

def test_string_with_two_numbers():
    # test with valid input (two comma separted numbers)
    assert string_calculator.add("1,2") == 3

def test_string_with_multiple_numbers():
    # test for multiple comma separated numbers
    assert string_calculator.add("1, 2, 3") == 6

def test_string_new_line():
    # Allow the Add method to handle new lines between numbers (instead of commas).
    assert string_calculator.add("1\n2,3") == 6
    assert string_calculator.add("1,\n, 2") == 3

def test_string_different_delimeters():
    # Support different delimiters
    assert string_calculator.add("//;\n1;2") == 3
    assert string_calculator.add('//[***][%]&\n1***2***3&5|1{}3') == 15

def test_string_with_negative_number():
    # For negative number it should throw an exception "negatives not allowed" with the number.
    with pytest.raises(Exception, match = r'negatives not allowed \[-1, -2\]'):
        string_calculator.add("2, -1, -2")

def test_string_with_alphabets():
    # test string with no numbers only string. It should return 0
    assert string_calculator.add("a, b") == 0

def test_number_with_underscore():

    assert string_calculator.add("1_000, 2_000") == 3000

def test_output_with_max_len():
    # Display can only show 6 digits on the screen, for more than 6 digits it should return #####
    # assert string_calculator.add("1_000000, 2_000000") == 3000000
    assert string_calculator.add("1_000000, 2_000000") == "######"
    assert string_calculator.add_2("1_000000, 2_000000") == "######"

def test_odd_even_index_scenario():

    assert string_calculator.add_2("1,3,4,7,6") == 1
    assert string_calculator.add_2("1,2") == -1
    assert string_calculator.add_2("") == 0
    assert string_calculator.add_2("2") == 2
    assert string_calculator.add_2("1\n2,3") == 2
    assert string_calculator.add_2("1,\n, 2") == -1
    assert string_calculator.add_2('//[***][%]&\n1***2***3&5|1{}3') == -5
    assert string_calculator.add_2("1_000, 2_000") == -1000


def test_terminal_calculator_output_for_add():
    # Test overflow of digits in terminal
    set_keyboard_input([1, "1_000000, 2_000000"])
    string_calculator.calculator()
    output = get_display_output()
 
    assert output == [
        'Select operation.',
        '1.Add numbers', 
        '2.Subtrace odd even sum',
        'Your option:',
        'Enter the string: ',
        '######'
    ]

    # Testing sum operations
    set_keyboard_input([1, "//[***][%]&\n1***2***3&5|1{}3"])
    string_calculator.calculator()
    output = get_display_output()
 
    assert output == [
        'Select operation.',
        '1.Add numbers', 
        '2.Subtrace odd even sum',
        'Your option:',
        'Enter the string: ',
        15
    ]
 
 
def test_terminal_calculator_output_for_add2():
    # Test overflow of digits in terminal
    set_keyboard_input([2, "1_000000, 2_000000"])
    string_calculator.calculator()
    output = get_display_output()
 
    assert output == [
        'Select operation.',
        '1.Add numbers', 
        '2.Subtrace odd even sum',
        'Your option:',
        'Enter the string: ',
        '######'
    ]
    # Test even odd calculation
    set_keyboard_input([2, "1,3,4,7,6"])
    string_calculator.calculator()
    output = get_display_output()
 
    assert output == [
        'Select operation.',
        '1.Add numbers', 
        '2.Subtrace odd even sum',
        'Your option:',
        'Enter the string: ',
        1
    ]
    # Test even odd calculation for negative output
    set_keyboard_input([2, "1,2"])
    string_calculator.calculator()
    output = get_display_output()
 
    assert output == [
        'Select operation.',
        '1.Add numbers', 
        '2.Subtrace odd even sum',
        'Your option:',
        'Enter the string: ',
        -1
    ]


def test_for_invalid_input_terminal():
    # Test for invalid input
    set_keyboard_input([4, "1_000000, 2_000000"])
    string_calculator.calculator()
    output = get_display_output()
 
    # print(output)
    assert output == [
        'Select operation.',
        '1.Add numbers', 
        '2.Subtrace odd even sum',
        'Your option:',
        'Invalid Input, Please choose 1 or 2',
    ]


def test_for_exceptions_terminal():
    # Test for exceptions
    set_keyboard_input([1, "1_000000, -2_000000"])
    string_calculator.calculator()
    output = get_display_output()
 
    # print(output)
    assert output == [
        'Select operation.',
        '1.Add numbers', 
        '2.Subtrace odd even sum',
        'Your option:',
        'Enter the string: ',
        'Negative not allowed',
    ]

