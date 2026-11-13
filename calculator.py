#Github link: https://github.com/sunandrew057/lab11-HO-AS/tree/main
#Partner 2: Hope Ong
#Partner 1: Andrew Sun
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def div(a, b):
    try:
        if a == 0:
            raise ZeroDivisionError
        return b / a
    except ZeroDivisionError:
        return("Cannot divide by 0")

def log(a, b):

def logarithm(a, b):
    try:
        if a < 2:
            raise ValueError
        return math.log(a, b)
    except ValueError:
        return "Can't take logarithm base less than 2"

def exp(a, b):
    return a**b

def exponent(a, b):
    return a**b
