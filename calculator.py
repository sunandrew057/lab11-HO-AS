"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def square_root(a):
    try:
        if a < 0:
            raise ValueError
        return math.sqrt(a)
    except ValueError:
        return "Cannot take square root of negative"

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        if a == 0:
            raise ZeroDivisionError
        return b / a
    except ZeroDivisionError:
        return("Cannot divide by 0")

def logarithm(a, b):
    try:
        if a < 2:
            raise ValueError
        return math.log(a, b)
    except ValueError:
        return "Can't take logarithm base less than 2"

def exponent(a, b):
    return a**b
