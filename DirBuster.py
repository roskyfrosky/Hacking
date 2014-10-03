#! /bin/python
from bs4 import BeautifulSoup
import sys,argparse,httplib

parser =argparse.ArgumentParser()
parser.add_argument("url", help="Input the url")
parser.add_argument("i",help="Input dictionary file")
parser.add_argument("-f","--FileOut",help="Output the result to a file", action="store", dest="outfile")
result = parser.parse_args()

found=[]

def req (m,n):
	con=httplib.HTTPConnection(m)		
	con.request('GET',n)		
	res =con.getresponse()
	if res.status == 200 :
		found.append(m+n)
	con.close()	

def main():
	inp = sys.argv[len(sys.argv)-1]
	op= open(inp,"r")
	url = sys.argv[len(sys.argv)-2]
	for line in op:
		if line.find(".") < 0:
			end=str("/"+line.strip("\n")+"/") #For directories
		else:
			end = str("/" +line.strip("\n")) #For files		
		req(url,end)			
	if result.outfile != None:
		f = open (result.outfile,"w");
		for x in found:
			f.write(x)
	else:
		for x in found:
			print x

if __name__=="__main__":
	main()

