"""create 10,000 random numbers and sum and product


"""
# the argument is passed to the function and assigned as the value to the parameter"""calculateSum returns the sum of a list argument, calculateProduct returns the product of the list argument

import random, sumproduct

numbers = []
for i in range(10000):
    numbers.append(random.randint(0,1000000))
print(f'Numbers: {numbers}')
print()
print(f'The sum of numbers is: {sumproduct.calculateSum(numbers):,}')
