#!/usr/bin/python 
# -*- coding: UTF-8 -*- 
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')

import urllib
import urllib2
import json
import time
import ssl
from bs4 import BeautifulSoup
context = ssl._create_unverified_context()
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
for bt in range(1,10):
	url = 'butian.360.cn/Reward/pub'
	d = {'w':'1', 'p':str(i),
		}
response = requests.post(url,data=d).text
print response.text