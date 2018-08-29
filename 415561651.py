#-----------------------------------------------------post请求ajax 
print(type(response)) 
url = '（这个地方我删掉了，大家根据自己需要访问的来写）' 
header={} 
header['Accept']='*/*' 
header['Accept-Encoding']='gzip, deflate' 
header['Accept-Language']='zh-CN,zh;q=0.8' 
header['Connection']='keep-alive' 
header['Content-Length']='6' 
header['Content-Type']='application/x-www-form-urlencoded' 
header['Host']='（这个地方我删掉了，大家根据自己需要访问的来写）' 
header['Origin']='（这个地方我删掉了，大家根据自己需要访问的来写）' 
header['Referer']='（这个地方我删掉了，大家根据自己需要访问的来写）' 
header['User-Agent']='（这个地方我删掉了，大家根据自己需要访问的来写）' 
header['X-Requested']='XMLHttpRequest' 
data ={'type':'3' } 
r=requests.post(url,data=data,headers=header) 
htmlcontent=r.content.decode('utf-8') 
s1=BeautifulSoup(htmlcontent,'lxml').find_all('div',class_ ='brief') 
for s in s1: 
print(s.div.contents[0]) 
#-------------------------------