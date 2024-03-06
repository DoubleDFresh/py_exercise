"""Converts a number of seconds into a str with the number of hours, minutes, and seconds

Given 600 (seconds), should return '10m' instead of '0h 10m 0s'
The only exception is given 0 (seconds), should return '0s'

Use join(), append(), lists, string concat

*** For an add'l challenge, break up 24 hour periods into days with a 'd' suffix - 90042 --> '1d 1h 42s'

"""
# the argument is passed to the function and assigned as the value to the parameter

def getHoursMinutesSeconds(totalSeconds):
    convertedTime = []
    if totalSeconds == 0:
        return '0s'
    if totalSeconds // 86400 > 0:
        convertedTime.append(str(totalSeconds // 86400) + 'd')
        totalSeconds %= 86400
    if totalSeconds // 3600 > 0:
        convertedTime.append(str(totalSeconds // 3600) + 'h')
        totalSeconds %= 3600
    if totalSeconds // 60 > 0:
        convertedTime.append(str(totalSeconds // 60) + 'm')
        totalSeconds %= 60
    if totalSeconds > 0:
        convertedTime.append(str(totalSeconds) + 's')
    return (' '.join(convertedTime))



assert getHoursMinutesSeconds(30) == '30s'
assert getHoursMinutesSeconds(60) == '1m'
assert getHoursMinutesSeconds(90) == '1m 30s'
assert getHoursMinutesSeconds(3600) == '1h'
assert getHoursMinutesSeconds(3601) == '1h 1s'
assert getHoursMinutesSeconds(3661) == '1h 1m 1s'
assert getHoursMinutesSeconds(90042) == '1d 1h 42s'
assert getHoursMinutesSeconds(0) == '0s'