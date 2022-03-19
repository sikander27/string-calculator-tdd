#!/usr/bin/python3

def string_calculator(s):
    print("String Calculator")
    if s == "":
        return 0
    numbers = list(map(int, s.split(",")))
    return sum(numbers)