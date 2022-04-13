#!/usr/bin/python3
# Display calculator, output > 5
import re

def add(s):
    """
    Args:
        s (string): string containing the numbers
    return:
       (int): sum of the numbers and 0 for empty string
    raises: negative not allowed exceptions
    """
    if helper_filter(s) == 0:
        return 0
    result = sum(helper_filter(s))
    digit_count = len(str(result))
    if digit_count > 6:
        return "######"
    
    return result


def add_2(s):
    """
    Args:
        s (string): string containing the numbers
    return:
       (int): sum of the numbers and 0 for empty string
    raises: negative not allowed exceptions
    """
    numbers = helper_filter(s)
    if numbers == 0:
        return 0
    even_sum, odd_sum = 0, 0
    for i in range(len(numbers)):
        if i%2 == 0:
            even_sum = even_sum + numbers[i]
        else:
            odd_sum = odd_sum + numbers[i]
    
    result = even_sum-odd_sum
    digit_count = len(str(result))
    if digit_count > 6:
        return "######"
    
    return result

def helper_filter(s):
    # Helper function to filter numbers
    if s == "": return 0
    s2 = s.replace("_", "")
    numbers = list(map(int, re.findall(r"-?\d+", s2)))
    negative_numbers = list(filter(lambda x: x < 0, numbers))
    if negative_numbers: raise Exception('negatives not allowed {}'.format(negative_numbers))

    return numbers

def calculator():

    print("Select operation.")
    print("1.Add numbers")
    print("2.Subtrace odd even sum")
    # take input from the user
    choice = input("Your option:")
    # check if choice is one of the four options
    if choice in (1, 2):
        input_string = input("Enter the string: ")
        try:
            if choice == 1:
                print(add(input_string))

            elif choice == 2:
                print(add_2(input_string))
        except:
            print("Negative not allowed")
    else:
        print("Invalid Input, Please choose 1 or 2")