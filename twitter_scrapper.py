# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 15:13:01 2017

@author: kishi
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import re
import time
import csv
import io
import pprint as pp

from time import sleep
import os
import sys
import pathlib
from timeit import default_timer as timer
import datetime

options = Options()
options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"
browser = webdriver.Chrome(chrome_options=options, executable_path="C:/chromedriver.exe", )

f = open('profiles.txt','r')
accounts = f.read()
p = accounts.split('\n')

PROFILE = p[:]

for ind in range(len(PROFILE)):
    url = PROFILE[ind]
    print('\n\nGetting followers from',url)

    f=open('completed.txt','a+')
    try:
        browser.get(url)
        sleep(5)
        s = str(browser.page_source)
        m = re.findall(' title="(.+?)"><span', s)
        flwrs=m[1]
        print(flwrs)
        f.write(url+' '+str(flwrs)+'\n')
        f.close()
    except:
        print('Skipping',url)
        f=open('completed.txt','a+')
        f.write(url+' '+' error'+'\n')
        f.close()