"""calculateSum returns the sum of a list argument, calculateProduct returns the product of the list argument

if the calculateSum(numbers) list is empty, return 0 - don't use sum()
if the calclateProduct(numbers) list is empty, return 1

"""
# the argument is passed to the function and assigned as the value to the parameter
def calculateSum(numbers):
    total = 0
    
    for elem in numbers:
        total += elem
    return total


def calculateProduct(numbers):
    total = 1

    for elem in numbers:
        total *= elem
    return total

assert calculateSum([]) == 0
assert calculateSum([2, 4, 6, 8, 10]) == 30
assert calculateProduct([]) == 1
assert calculateProduct([2, 4, 6, 8, 10]) == 3840
