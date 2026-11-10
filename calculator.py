# https://github.com/sunandrew057/lab11-HO-AS.git
# Partner 1: Andrew Sun
# Partner 2: Hope Ong

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        if a == 0:
            raise ZeroDivisionError
        return b / a
    except ZeroDivisionError:
        return("Cannot divide by 0")

def logarithm(a, b):
    if a < 2:
        raise ValueError
    return math.log(a, b)

def exp(a, b):
    return a**b
