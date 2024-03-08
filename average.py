"""An average function that has a numbers parameter

Don't use the sum() function
An empty list returns None

"""
# the argument is passed to the function and assigned as the value to the parameter"""calculateSum returns the sum of a list argument, calculateProduct returns the product of the list argument
import random, sumproduct

def average(numbers):
    answer = 0
    if len(numbers) == 0:
        return None
    return sumproduct.calculateSum(numbers) / len(numbers)

assert average([1, 2, 3]) == 2
assert average([1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2
assert average([12, 20, 37]) == 23
random.seed(42)
testData = [1, 2, 3, 1, 2, 3, 1, 2, 3]
for i in range(1000):
    random.shuffle(testData)

assert average(testData) == 2