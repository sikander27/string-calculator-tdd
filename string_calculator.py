#!/usr/bin/python3
import re

def add(s):
    if s == "": return 0
    numbers = list(map(int, re.findall(r"-?\d+", s)))
    # import pdb; pdb.set_trace()
    negative_numbers = []
    for i in numbers:
        if i < 0:
            negative_numbers.append(i)
    if negative_numbers:
        raise Exception('negatives not allowed {}'.format(negative_numbers))
    return sum(numbers)