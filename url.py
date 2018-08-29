import urllib
import urllib2
import json
import requests
from bs4 import BeautifulSoup 

response = requests.get('http://butian.360.cn/Company/99').text
soup = BeautifulSoup(response,'html.parser')
name = {i.text for i in soup.findAll('div',{'class':'firmName1'})}
for s in name:
print (s) 