#!/usr/bin/env python3
# stripString.py

import re

def stripString(text, char = None):
    prefixSpaceRegex = re.compile(r'^\s+')
    suffixSpaceRegex = re.compile(r'\s+$')

    text = prefixSpaceRegex.sub('', text)  # Strip leading spaces
    text = suffixSpaceRegex.sub('', text)  # Strip ending spaces

    # Remove characters provided in second arguments
    if char != None:
        # charRegex = re.compile(f'[{str(char)}]')
        charRegex = re.compile(r'[' + re.escape(char) + r']')
        text = charRegex.sub('', text)

    return text


mytext = r'     3238 .,  !@#$%^&*()[]{}   asdfasdfas dfasdfs.  x   .           '

outtext = stripString(mytext, 'xs,.a^*2')

print(len(outtext) * '-')
print(outtext)
