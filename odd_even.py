"""Determine if a number is odd or even

Two functions to determine if a number is odd or even
isOdd(number) takes an input and returns True if odd; False if even
- returns False for all floats
- returns False for an input of 0

isEven(number) takes an input and returns True if even; False if odd
- returns False for all floats
- returns True for an input of 0
"""
# the argument is passed to the function and assigned as the value to the parameter

def isOdd(number):
    return number % 2 == 1

def isEven(number):
    return number % 2 == 0

assert isOdd(42) == False
assert isOdd(9999) == True 
assert isOdd(-10) == False 
assert isOdd(-11) == True 
assert isOdd(3.1415) == False
assert isEven(42) == True 
assert isEven(9999) == False 
assert isEven(-10) == True 
assert isEven(-11) == False 
assert isEven(3.1415) == False

