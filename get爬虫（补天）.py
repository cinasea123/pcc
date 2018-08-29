import urllib
import urllib2
import json
import requests
from bs4 import BeautifulSoup 

for page in range(32,61015):
	url = 'http://butian.360.cn/Company/%d/' %page
	response = requests.get(url).text
	soup = BeautifulSoup(response,'html.parser')
	for i in soup.find_all('div',{'class':'firmName1'}):
		print i.text



		