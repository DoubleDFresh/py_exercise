"""4 Functions to calculate area, perimeter, volume, & surface area


"""
# the argument is passed to the function and assigned as the value to the parameter

def area(length, width):
    return length * width

def perimeter(length, width):
    return (2 * length) + (2 * width)

def volume(length, width, height):
    return (length * width * height)

def surfaceArea(length, width, height):
    # updated to remove redunant * 2
    return ((length * width) + (length * height) + (width * height)) * 2

assert area(10, 10) == 100 
assert area(0, 9999) == 0 
assert area(5, 8) == 40 
assert perimeter(10, 10) == 40 
assert perimeter(0, 9999) == 19998 
assert perimeter(5, 8) == 26
assert volume(10, 10, 10) == 1000 
assert volume(9999, 0, 9999) == 0 
assert volume(5, 8, 10) == 400 
assert surfaceArea(10, 10, 10) == 600 
assert surfaceArea(9999, 0, 9999) == 199960002 
assert surfaceArea(5, 8, 10) == 340
