#!/usr/bin/python3
import re

def add(s):
    if s == "": return 0
    numbers = list(map(int, re.findall(r"\d+", s)))
    return sum(numbers)