"""Determine if number (upTo) is divisible by 3, 5, or both
return:
- 'FizzBuzz' if divisible by 3 and 5
- 'Fizz' if only divisible by 3
- 'Buzz' if only divisible by 5
- just the value if neither divisible by 3 or 5

Example: upTo = 15 --> 1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz

"""
# the argument is passed to the function and assigned as the value to the parameter

def fizzBuzz(upTo):
    # start at 1, print 'Fizz' or number
    answer = ''
    for number in range(1, upTo + 1):
        if (number % 3 != 0) and (number % 5 != 0):
            answer += str(number) + ' '
        elif (number % 3 == 0) and (number % 5 != 0):
            answer += 'Fizz '
        elif (number % 3 != 0) and (number % 5 == 0):
            answer += 'Buzz '
        else:
            answer += 'FizzBuzz '
    return answer

print(fizzBuzz(35))