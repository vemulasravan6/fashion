# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

#binary = FirefoxBinary('/home/vemula/Downloads/firefox-32.0/firefox/firefox')
#driver = webdriver.Firefox(firefox_binary=binary)
#driver.get('https://google.com')

#driver = webdriver.Firefox()
#print(driver)

#
#   54.179.195.230 atlas-competitive-intelligence-16
#   54.151.187.156 atlas-competitive-intelligence-17
#

import wget
import gzip

import subprocess
data_download_status = False
data = None
shell_cmd = None
import os

#print('Beginning file download with wget module')

url = 'https://www.lefties.com/9/info/sitemaps/sitemap-home-categories-lf-mx-0.xml.gz'

def readDataFromUrl(url):
    path = url.split('/')[-1]
    data_download_status = False
    file_content = ''
    shell_cmd = "wget -O " + path + " -q " + url
    try:
        data = subprocess.Popen(shell_cmd, shell=True, stdout=subprocess.PIPE).stdout.read()
        data_download_status = True
        f = gzip.open(path, 'rb')
        file_content = f.read().lower()
        f.close()
        os.remove(path)
    except:
        data = None
        print("HTML_DOWNLOAD_EXCEPTION")
        pass
    return file_content,data_download_status

#print(readDataFromUrl('https://www.lefties.com/9/info/sitemaps/sitemap-home-categories-lf-es-0.xml.gz'))

#print(data)
#wget.download(url, path)
#f = gzip.open(path, 'rb')
#report = f.read().lower()
#f.close()
