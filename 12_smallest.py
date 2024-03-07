"""re-implement min() function by finding the smallest number in a list.  another fn returns the biggest number

Takes a list of ints / floats and returns the smallest value / biggest value depending upon the function name
If the list is empty, return 'None'

"""
# the argument is passed to the function and assigned as the value to the parameter

def getSmallest(numList):
    
    if len(numList) == 0:
        return None
    baseValue = numList[0]
    
    for elem in numList:
        if elem < baseValue:
            baseValue = elem
    return baseValue

def getBiggest(numList):
    baseValue = 0
    if len(numList) == 0:
        return None
    for elem in numList:
        if elem > baseValue:
            baseValue = elem
    return baseValue

assert getSmallest([1, 2, 3]) == 1
assert getSmallest([3, 2, 1]) == 1 
assert getSmallest([28, 25, 42, 2, 28]) == 2 
assert getSmallest([1]) == 1
assert getSmallest([]) == None

assert getBiggest([1, 2, 3]) == 3
assert getBiggest([3, 2, 1]) == 3
assert getBiggest([28, 25, 42, 2, 28]) == 42
assert getBiggest([1]) == 1
assert getBiggest([]) == None