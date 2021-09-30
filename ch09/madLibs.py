#!/usr/bin/env python3
# madLibs.pyw


# python madLibs.pyw <file> - Replaces the keywords with user input words
# Keywords: ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']

import re
import sys
import pyinputplus as pyip
from pathlib import Path

# Check if command is correct
if len(sys.argv) != 2:
    print('Usage: python madLibs.pyw <file>')
    sys.exit()

# Open and read text file
file = Path(sys.argv[1])
print(file)
sentence = file.read_text()

# Create regex out of list of words to replace
wordList = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']
wordRegex = re.compile('|'.join(wordList))
# Find words to replace from the sentence
replaceList = wordRegex.findall(sentence)

# Loop through each replace list and replace it by user's input
for replace in replaceList:
    prompt = f'Enter an {replace.lower()}:\n'
    word = pyip.inputStr(prompt)
    sentence = wordRegex.sub(word, sentence, count=1)

# Write the replaced sentence to the text file
file.write_text(sentence)