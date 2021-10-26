#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# downloadXkcd.py - Download every single XKCD comic.
'''
Loads XKCD home page
Saves comic image on the page
Follows previous comic link
Repeats until first comic
'''

import requests
import os
import bs4
from pathlib import Path

url = 'https://xkcd.com'      # starting url
dir = Path('xkcd')            # store comics in ./xkcd
dir.mkdir(exist_ok=True)

while not url.endswith('#'):
    # Download the page.
    print(f'Downloading page {url}...')
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = 'https:' + comicElem[0].get('src')

        # Download the image.
        print(f'Downloading image {comicUrl}...')
        res = requests.get(comicUrl)
        res.raise_for_status()

        # Save the image to ./xkcd.
        imageFile = open(dir / Path(comicUrl).name, 'wb')

        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')

print('Done.')