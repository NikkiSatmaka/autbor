#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# insertGaps.py - insert gaps at position x for file names with prefix

import enum
import os
import re
import shutil
from pathlib import Path

def insertGaps(folder, prefix, position):
    dir = Path(folder).absolute()

    fileRegex = re.compile(r'(^' + re.escape(prefix) + r')' + r'(\d*)' \
        + r'(\..*$)')

    fileList = [file for file in dir.glob(f'{prefix}*')]

    # Loop through each files and regex search
    for index, file in enumerate(fileList[::-1]):
        # Check position
        if position > len(fileList):
            print('Position is outside of file list range. Not renaming anything')
            break

        mo = fileRegex.search(file.name)
        fileNumber = int(mo.group(2))
        ext = mo.group(3)

        # Stop after getting to the position to insert
        if index == len(fileList) - position:
            print("Do not rename", index, file.name)
            break

        newFile = dir / f'{prefix}{fileNumber+1:03d}{ext}'
        print(f'Renaming {file.name} to {newFile.name}')
        file.rename(newFile)

insertGaps(r'C:\example', 'spam', 3)