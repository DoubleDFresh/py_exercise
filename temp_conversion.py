"""Convert C to F & F to C

Two functions for temp.
convertToFahrenheit takes an int and returns a float in Fahrenheit
convertToCelsius takes an int and returns a float in Celsius
"""
# the argument is passed to the function and assigned as the value to the parameter


def convertToFahrenheit(degreeCelsius):
    return (degreeCelsius * 9/5) + 32

def convertToCelsius(degreeFahrenheit):
    return (degreeFahrenheit - 32) * 5/9
            

assert convertToCelsius(0) == -17.77777777777778 
assert convertToCelsius(180) == 82.22222222222223 
assert convertToFahrenheit(0) == 32 
assert convertToFahrenheit(100) == 212 
assert convertToCelsius(convertToFahrenheit(15)) == 15