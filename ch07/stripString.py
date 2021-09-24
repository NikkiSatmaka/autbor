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
        charRegex = re.compile(f'[{str(char)}]')
        text = charRegex.sub('', text)

    return text


mytext = '     3238      asdfasdfas dfasdfs.  x   .           '

outtext = stripString(mytext, 'xsa2')

print(len(outtext) * '-')
print(outtext)
