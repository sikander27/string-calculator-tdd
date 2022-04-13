"""
This file contains the helper mocking functions
"""
import builtins

input_values = []
print_values = []

# Function to mock inputs
def mock_input(s):
    print_values.append(s)
    return input_values.pop(0)

# Function to mock input output/print
def mock_input_output_start():
    global input_values, print_values

    input_values = []
    print_values = []

    builtins.input = mock_input
    builtins.print = lambda s: print_values.append(s)

# Function to return output/print values
def get_display_output():
    global print_values
    return print_values

# Function to set mock inputs
def set_keyboard_input(mocked_inputs):
    global input_values

    mock_input_output_start()
    input_values = mocked_inputs
