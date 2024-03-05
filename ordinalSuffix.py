"""Takes an integer and and returns a string of the number with its ordinal suffix

cardinal numbers refer to the size of a group of objects (*four* balls, *1,000* tickets)
ordinal numbers refer to the place of an object in ordered sequence (*first* place, *30th* birthday)

ordinal numbers have 'th' as in 20th or 'nd' as in 2nd.
'th' end with 11,12,13 or any numbers not met below
'st' end with 1
'nd' end with 2
'rd' end with 3

"""
# the argument is passed to the function and assigned as the value to the parameter

def ordinalSuffix(number):
    if number % 100 in (11,12,13):
        return str(number) + 'th'
    if number % 10 == 1:
        return str(number) + 'st'
    if number % 10 == 2:
        return str(number) + 'nd'
    if number % 10 == 3:
        return str(number) + 'rd'
    return str(number) + 'th'

assert ordinalSuffix(0) == '0th' 
assert ordinalSuffix(1) == '1st' 
assert ordinalSuffix(2) == '2nd' 
assert ordinalSuffix(3) == '3rd' 
assert ordinalSuffix(4) == '4th' 
assert ordinalSuffix(10) == '10th' 
assert ordinalSuffix(11) == '11th' 
assert ordinalSuffix(12) == '12th' 
assert ordinalSuffix(13) == '13th' 
assert ordinalSuffix(14) == '14th' 
assert ordinalSuffix(101) == '101st'

