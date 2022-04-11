#!/usr/bin/python3
# Display calculator, output > 5
from dataclasses import replace
import re

def add(s):
    """
    Args:
        s (string): string containing the numbers
    return:
       (int): sum of the numbers and 0 for empty string
    raises: negative not allowed exceptions
    """

    return 0 if helper_filter(s) == 0 else sum(helper_filter(s)) 

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
    
    return even_sum-odd_sum

def helper_filter(s):
    # Helper function to filter numbers
    if s == "": return 0
    s2 = s.replace("_", "")
    numbers = list(map(int, re.findall(r"-?\d+", s2)))
    negative_numbers = list(filter(lambda x: x < 0, numbers))
    if negative_numbers: raise Exception('negatives not allowed {}'.format(negative_numbers))

    return numbers