#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# selectiveCopy.py - copy certain file extension to a new folder

import re
import os
import shutil
from pathlib import Path

def selectiveCopy(dir, ext):
    # regex is (filename)(.)(ext)
    extRegex = re.compile(r'(^.*)(\.)' + r'(' + re.escape(ext) + r'$)',
        re.IGNORECASE)

    dir = Path(dir).absolute()

    # Figure out the dirname this code should use based on
    # what directory already exist.
    number = 1
    while True:
        targetDir = dir / f'{ext}_files_{number}'
        if not targetDir.exists():
            break
        number += 1
    
    # Create target directory.
    print(f'Creating dir {targetDir}')
    targetDir.mkdir()

    for dirpath, dirnames, filenames in os.walk(dir):
        dirpath = Path(dirpath)
        # Do not check the target folder or any version of it
        newBase = f'{ext}_files_'
        if dirpath.name.startswith(newBase):
            continue

        for filename in filenames:
            mo = extRegex.search(filename)
            if mo != None:
                filename = dirpath / filename
                print(f'Copying {filename} to {targetDir}')
                shutil.copy(filename, targetDir)

selectiveCopy(r'C:\example', 'txt')