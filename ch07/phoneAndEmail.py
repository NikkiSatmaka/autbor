#!/usr/bin/env python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

'''
1. Get text of clipboard
2. Find all phone numbers and email addresses
3. Paste them into clipboard


1. Use pyperclip to copy paste string
2. Create 2 regexes, 1 for phone numbers and 1 for emails
3. Find all matches of both regexes
4. Format all matched strings into a single string
5. Display message if no matches were found
'''

import pyperclip, re

# Create phone regex.
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator 
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)


# Create email regex.
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+    # username
    (@)                  # @ symbol
    [a-zA-Z0-9.-]+       # domain name
    (\.[a-zA-Z]{2,4})    # dot-something
    )''', re.VERBOSE)


# Find matches in clipboard text.
text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])


# TODO: Copy results to clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')