#!/usr/bin/env python3
# regexSearch.py

# python regexSearch.py [regex] <folder>

import re
import sys
from pathlib import Path

# Check for terminal usage
if len(sys.argv) != 3:
    print('Usage: python regexSearch.py [regex] <folder>')
    sys.exit()

# Compile the regex
userRegex = re.compile(sys.argv[1])

# Open files in folder
workingDir = Path(sys.argv[2])
filesList = list(workingDir.glob('*.txt'))

# Loop through each file, read every lines and store it as list
for file in filesList:
    linesList = open(str(file)).readlines()
    # Loop through each line and search regex
    for line in linesList:
        mo = userRegex.search(line)
        if mo == None: # If no regex found, pass
            continue
        # Print out the line without the \n line break
        print(f'{str(file.name)}: "{line[:-1]}"')