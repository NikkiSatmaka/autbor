#!/usr/bin/env python3
# idiotBusy.py

'''
1. Ask if they'd like to know how to keep an idiot busy for hours.
2. If user answers no, quit
3. If user answers yes, go step 1
'''

import pyinputplus as pyip

while True:
    prompt = 'Want to know how to keep an idiot busy for hours?\n'
    response = pyip.inputYesNo(prompt)
    if response == 'no':
        break

print('Thank you. Have a nice day.')