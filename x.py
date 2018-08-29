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
doc=open('text.txt','w')
context = ssl._create_unverified_context()
url = 'http://butian.360.cn/Reward/pub'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
for i in range(1,2):
	data = urllib.urlencode({'s': 1, 'p':i})
	request = urllib2.Request(url, headers = headers)
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor()) 
	response = opener.open(request, data) 
	result = response.read()
	#jx = json.dumps(json.loads(result),ensure_ascii=False)
	all = json.loads(result)['data']['list']
	sea = (list(all))
	for bt in sea:
		print bt['company_name']
		doc.write(bt['company_name'] + '\n')
doc.close()