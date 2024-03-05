"""Prints the ASCII number and its corresponding text char from 32 thru 126
use the ord() and char() functions

"""
# the argument is passed to the function and assigned as the value to the parameter

def printASCIITable():
    for num in range(32,127):
        print(num, chr(num))

printASCIITable()