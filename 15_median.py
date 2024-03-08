"""returns the median of a numbers list
The median of an odd-length list is the middle when the list is sorted
If the list is even-length, the median is the average of the 2 middle-most numbers when sorted
An empty list should return None

"""
import average, random

def median(numbers):
    if len(numbers) == 0:
        return None
    
    numbers.sort()
    mid = len(numbers) // 2

    if len(numbers) % 2 == 1:
        return numbers[mid]
    else:
        return ((numbers[mid - 1]) + numbers[mid]) / 2

assert median([]) == None
assert median([1, 2, 3]) == 2
assert median([3, 7, 10, 4, 1, 9, 6, 5, 2, 8]) == 5.5
assert median([3, 7, 10, 4, 1, 9, 6, 2, 8]) == 6
random.seed(42)
testData = [3, 7, 10, 4, 1, 9, 6, 2, 8]
for i in range(1000):
    random.shuffle(testData)
assert median(testData) == 6