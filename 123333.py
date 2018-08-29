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
a={"s":1,"p":20}
r=requests.post("http://butian.360.cn/Reward/pub",data=json.dumps(a))
soup=BeautifulSoup.BeautifulSoup(r.text)
print soup