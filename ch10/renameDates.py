#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# renameDates.py - Rename files with American MM-DD-YYY date format
# to European DD-MM-YYY.

'''
1. Search all filenames in cwd for american-style dates
2. Rename file with month and day swapped to european-style

1. Create regex for american-style dates
2. Find all files in working directory
3. Loop over each file, check using regex for dates
4. If it has a date, rename file
'''

import shutil, os, re
from pathlib import Path

# Create a regex that matches file with the American date format.

datePattern = re.compile(r"""^(.*?)   # all text before the date
    ((0|1)?\d)-                       # one or two digits for the month
    ((0|1|2|3)?\d)-                   # one or two digits for the day
    ((19|20)\d\d)                     # four digits for the year
    (.*?)$                            # all text after the date
    """, re.VERBOSE)

# Loop over the files in the working directory.
for amerFilename in list(Path.cwd().glob('*')):
    mo = datePattern.search(amerFilename.name)
    # Skip files without date.
    if mo == None:
        continue

    # Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # Form the European-style filename.
    euroFilename = f'{beforePart}{dayPart}-{monthPart}-{yearPart}{afterPart}'

    # Get the full, absolute file paths.
    absWorkingDir = Path.cwd()
    euroFilename = absWorkingDir / euroFilename

    # Rename the files.
    print(f'Renaming "{amerFilename}" to "{euroFilename}"...')
    shutil.move(amerFilename, euroFilename)    # uncomment after testing