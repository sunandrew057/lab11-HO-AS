"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def add(a, b): 
    pass

import math

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a*b

def div(a,b):
    if a == 0:
        raise ZeroDivisionError ("ZeroDivisionError! a cannot equal 0")
    return b/a

def log(a,b):
    if b == 0:
        raise ValueError ("ValueError")
    return math.log(b,a)

def exp(a ,b):
    return a**b
