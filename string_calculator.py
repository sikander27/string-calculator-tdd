#!/usr/bin/python3
import re

def add(s):
    """
    Args:
        s (string): string containing the numbers
    return:
       (int): sum of the numbers and 0 for empty string
    raises: negative not allowed exceptions
    """
    if s == "": return 0
    numbers = list(map(int, re.findall(r"-?\d+", s)))
    negative_numbers = list(filter(lambda x: x < 0, numbers))
    if negative_numbers: raise Exception('negatives not allowed {}'.format(negative_numbers))
    return sum(numbers)