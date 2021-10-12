#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# massiveFileDetector.py - search through folder recursively
# for files with size above 100MB

import os
from pathlib import Path

def massiveFileDetector(dir, size):
    # Enter size filter in MB
    size_limit = size
    dir = Path(dir).absolute()

    for dirpath, dirnames, filenames in os.walk(dir):
        dirpath = Path(dirpath)

        dirsize = 0
        for filename in filenames:
            filename = dirpath / filename
            filesize = os.path.getsize(filename)
            dirsize += filesize
            # if filesize / (1024 * 1024) > size_limit:
            #     print(f'{filename.name} | {filesize / (1024 * 1024):.1f} MB')

        # Detect directory size
        if dirsize / (1024 * 1024) > size_limit:
            print(f'{dirpath} | {dirsize / (1024 * 1024):.1f} MB')
        

massiveFileDetector('C:\example', 100)