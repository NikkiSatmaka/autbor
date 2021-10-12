#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# fillingGaps.py - fill the number gaps for files with prefix

import re
from pathlib import Path

def fillingGaps(folder, prefix):
    dir = Path(folder).absolute()

    # regex is spam001.txt and such
    fileRegex = re.compile(r'(^' + re.escape(prefix) + r')' + r'(\d*)' \
        + r'(\..*$)')

    # Loop through each files and regex search
    for index, file in enumerate(dir.glob(f'{prefix}*')):
        mo = fileRegex.search(file.name)
        fileNumber = int(mo.group(2))
        ext = mo.group(3)

        # index 0 is file 001 and so on
        if index + 1 != fileNumber:
            newFile = dir / f'{prefix}{index + 1:03d}{ext}'
            print(f"Renaming file '{file.name}' to '{newFile.name}'")
            file.rename(newFile)

fillingGaps(r'C:\example', 'spam')