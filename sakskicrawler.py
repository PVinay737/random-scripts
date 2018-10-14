import requests
import urllib2
from bs4 import BeautifulSoup
import lxml
import numpy as np

links=[]
for i in range(1,501):
	seed="https://www.sakshi.com/news/sports?new=1534517988&page="+str(i) 
	url = urllib2.urlopen(seed)
	content = url.read()
	soup = BeautifulSoup(content,"html.parser" )

	#print soup
	for row in soup('div', {'class':'views-field views-field-title'} ):
		for j in row.find_all('span'):
			for k in j.find_all('a'):
				k=str(k)
				k=k.split('>')
				m=k[0]
				m=m.strip('<a href=')
				m=m.strip('"')
				seed=seed.strip('?new=1534517988&page='+str(i))
				seed=seed.strip('/news/sports')
				link=seed+m
				links.append(link)
		#		print link

data=[]
#print len(links)
for i in range(len(links)):
	#print links[i]
	info=urllib2.urlopen(links[i])
	info_content=info.read()
	soup = BeautifulSoup(info_content,"html.parser" )
	
	for m in soup('p',{'class':'rtejustify'}):
		print (m.text).encode('UTF-8')
		data.append((m.text))
		np.savetxt('crawled_result',data,fmt='%s')
