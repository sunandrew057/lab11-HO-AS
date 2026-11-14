# https://github.com/sunandrew057/lab11-HO-AS.git
# Partner 2: Hope Ong
# Partner 1: Andrew Sun

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
    if a == 0:
        raise ZeroDivisionError
    return b / a

def logarithm(a, b):
    if a < 2:
        raise ValueError
    return math.log(b, a)

def exp(a, b):
    return a**b
