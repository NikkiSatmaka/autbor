#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import zipfile, os
from pathlib import Path

def backupToZip(folder):
    # Back up the entire contents of "folder" into a ZIP file.

    folder = Path(folder).absolute()    # make sure folder is absolute

    # Figure out the filename this code should use based on
    # what files already exist.
    number = 1
    while True:
        zipFilename = f'{folder.name}_{number}.zip'
        if not Path(zipFilename).exists():
            break
        number += 1
    
    # Create the ZIP file.
    print(f'Creating {zipFilename}...')
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Adding files in {foldername}...')
        # print(f'Adding files in {Path(foldername).relative_to(folder.parent)}...')
        foldername = Path(foldername)
        folderarcname = foldername.relative_to(folder.parent)
        # Add the current folder to the ZIP file.
        backupZip.write(foldername, arcname=folderarcname)

        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            newBase = folder.name + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue    # don't back up the backup ZIP files
            filename = foldername / filename
            filearcname = filename.relative_to(folder.parent)
            backupZip.write(foldername / filename, arcname=filearcname)

    # # Pathlib version
    # # Walk the entire folder tree and compress the files in each folder.
    # for file in folder.rglob('*'):
    #     filearcname = file.relative_to(folder.parent)
    #     newBase = folder.name + '_'
    #     if file.name.startswith(newBase) and file.name.endswith('.zip'):
    #         continue    # don't back up the backup ZIP files
    #     backupZip.write(file, arcname=filearcname)

    print('Done.')

backupToZip(r'C:\example')