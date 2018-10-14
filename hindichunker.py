#!/usr/bin/python
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import json
import urllib
import urllib3
import sys
import time

def ilmtApi(first, last, text):
    pool = urllib3.PoolManager()
    time.sleep(0.9) 	
    url = 'http://api.ilmt.iiit.ac.in/hin/pan/%s/%s' % (first, last)
    method = 'POST'
    headers = {'Content-Type':'application/x-www-form-urlencoded', 'charset':'UTF-8'}
    data = pool.urlopen(method, url, headers = headers, body = text).data
    return json.loads(data)

def check_float(word_encoded):
    try:
        if float(word_encoded):
            return True
    except ValueError:
        return False


def get_phrases(sentence):

#    try:
	tillChunker = ilmtApi('1', '10', "input=%s" % (sentence))
	payload = "input=" + urllib.quote(tillChunker['chunker-5'].encode('UTF-8'))
        wx2utf = ilmtApi('14', '14', payload)["wx2utf-14"]
        text= wx2utf.split()
        check=0
        phrase_set=[]
        phrase=""
	final=[]
	lt=[]
	mm=[]
        for word in text:		
            word_encoded=word.encode('UTF-8')
            if check_float(word_encoded):
            	if check==int(float(word_encoded)):
  	    		phrase=phrase+text[text.index(word_encoded)+1].strip()+" "
			final.append(phrase)
			lt.append(len(phrase))
			#print final[len(final)-1],len(final),len(phrase)
			mm=zip(final,lt)										 
	   	else:
              		check=int(float(word_encoded))
			#print phrase
                	if phrase!="":
		    		#print phrase
                    		phrase_set.append(phrase)
		    		phrase=""
     	return mm

def main():
    path = "~/Desktop/phrase-translation/IN-DOMAIN/MachineTranslation/chunk_test/splitbyfiles"
    dirs = os.listdir( path )
    if not os.path.exists('chunker_outputs'):
        os.makedirs('chunker_outputs')
    for i in range(1,501):
    data=open(file_name,'r')
    f=open('chunks.txt','w')
    count=0;
    x=[]
    for line in data:
    	time.sleep(0.1) 	
        phrase_set=get_phrases(line)
	x.append(phrase_set)
	y=x[len(x)-1]
	#print y	
	for i in range(len(y)):
		if(i+1 < len(y)):	
			if(y[i][1] > y[i+1][1]):
				print y[i][0]
		else:
			print y[i][0]		
							
main()
