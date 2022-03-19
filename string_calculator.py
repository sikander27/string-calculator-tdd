#!/usr/bin/python3

def add(s):
    print("String Calculator")
    if s == "":
        return 0
    numbers = list(map(int, s.split(",")))
    return sum(numbers)