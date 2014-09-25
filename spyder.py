#! /bin/python
from bs4 import BeautifulSoup
import urllib2,urllib,sys, argparse

def search(d):
	content= urllib2.urlopen(d).read()
	soup= BeautifulSoup(content)
	for link in soup.find_all('a',href=True):	
		aux.append(link['href'])

url=sys.argv[1]
aux=[]
search(url)
print aux
