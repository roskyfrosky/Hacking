#! /bin/python
from bs4 import BeautifulSoup
import urllib,sys,argparse,httplib

parser =argparse.ArgumentParser()
parser.add_argument("url", help="Input the url")
parser.add_argument("-f","--FileOut",help="Output the result to a file", action="store", dest="outfile")
parser.parse_args()

HiddenDir= ["/system/", "/manager/","/admin/","/administrator/"]
found=[]
def main():
	i=0
	while i < len (HiddenDir): 
		url = sys.argv[len(sys.argv)-1]
		end = HiddenDir[i]
		con=httplib.HTTPConnection(url)	
		con.request('GET',end)
		res =con.getresponse()
		if res.status == 200 :
			found.append(url+end)					
			
				
		i+=1	
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
