#!/usr/bin/env python3
# dateDetector.py

import re

# Date regex
dateRegex = re.compile(r'''(
    (0[1-9]|[1-2]\d|3[0-1])    # day
    /                          # separator
    (0[1-9]|1[0-2])            # month
    /                          # separator
    ([1-2]\d{3})               # year (1000-2999)
    )''', re.VERBOSE)

# Leap year detector
def leapYear(year):
    isLeapYear = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                isLeapYear = True
        else:
            isLeapYear = True
    return isLeapYear

# Date validator
def dateValidator(day, month, year):
    # April, June, September or November
    if month in [4, 6, 9, 11]:
        if day > 30:  # Max 30 days
            return False
        else:
            return True
    # February
    elif month == 2:
        if leapYear(year):  # Leap year max days 29
            if day > 29:
                return False
            else:
                return True
        elif day > 28:  # Not leap year max days 28
            return False
        else:
            return True
    # Regex has made sure max day is 31
    else:
        return True

date = '29/10/1993 32/32/2910 31/02/2000 29/02/2000'

result = {}

for groups in dateRegex.findall(date):
    day = int(groups[1])
    month = int(groups[2])
    year = int(groups[3])

    result[groups[0]] = dateValidator(day, month, year)

print(result)