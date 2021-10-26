#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# auto2048.py

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

url = 'https://play2048.co/'
browser.get(url)

htmlElem = browser.find_element_by_tag_name('html')
while True:
    htmlElem.send_keys(Keys.ARROW_UP)
    htmlElem.send_keys(Keys.ARROW_RIGHT)
    htmlElem.send_keys(Keys.ARROW_DOWN)
    htmlElem.send_keys(Keys.ARROW_LEFT)