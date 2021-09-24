#!/usr/bin/env python3

import re

lenRegex = re.compile(r'.{8,}')
lowerRegex = re.compile(r'[a-z]')
upperRegex = re.compile(r'[A-Z]')
digitRegex = re.compile(r'\d')

mypass = 'asD3d'

def passwordDetector(password):
    if lenRegex.search(password) == None:
        print('Password must be at least 8 characters long.')
        return False
    elif lowerRegex.search(password) == None:
        print('Password must contain a lower case letter.')
        return False
    elif upperRegex.search(password) == None:
        print('Password must contain an upper case letter.')
        return False
    elif digitRegex.search(password) == None:
        print('Password must contain at least 1 digit.')
        return False
    else:
        print('Password is strong.')
        return True

passwordDetector(mypass)