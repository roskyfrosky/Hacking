#! /bin/python
from bs4 import BeautifulSoup
import sys,argparse,httplib

parser =argparse.ArgumentParser()
parser.add_argument("url", help="Input the url")
parser.add_argument("i",help="Input dictionary file")
parser.add_argument("-f","--FileOut",help="Output the result to a file", action="store", dest="outfile")
result = parser.parse_args()

found=[]
def main():
	inp = sys.argv[len(sys.argv)-1]
	op= open(inp,"r")
	for line in op:
		url = sys.argv[len(sys.argv)-2]
		con=httplib.HTTPConnection(url)		
		end=str("/"+line.strip("\n")+"/")
		con.request('GET',end)		
		res =con.getresponse()
		if res.status == 200 :
			found.append(url+end)				
	con.close()
	
	if result.outfile != None:
		f = open (result.outfile,"a");
		for x in found:
			f.write(x)
	else:
		for x in found:
			print x

if __name__=="__main__":
	main()
