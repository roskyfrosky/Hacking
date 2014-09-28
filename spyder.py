#! /bin/python
from bs4 import BeautifulSoup
import urllib2,urllib,sys,argparse

parser =argparse.ArgumentParser()
parser.add_argument("url", help="Input the url to Spyder")
parser.add_argument("-o","--output",help="Output the result to a file", action="store_true")
args=parser.parse_args()


def search(d):
	content= urllib2.urlopen(d).read()
	soup= BeautifulSoup(content)
	for link in soup.find_all('a',href=True):	
		string= d+link['href'] +"\n"
		if i==1 :	
			f.write(string)
		else:		
			print string
def main():
	global i ,f
	i=0	
	url=sys.argv[len(sys.argv)-1] #url start
	if args.output:
		f=open("OutSpyder.txt","a")
		i=1
	search(url)
	if i==1:
		f.close()

if __name__=="__main__":
	main()
