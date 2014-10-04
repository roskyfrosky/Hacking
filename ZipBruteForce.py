#! /bin/python
import zipfile,sys,argparse, os
from threading import Thread

parser=argparse.ArgumentParser()
parser.add_argument("ZipFile",help="The Zip file with password ")
parser.add_argument("Dicctionary",help="Dicctionary with passwords")
parser.add_argument("-D","--DPath", help="Destination path for the extracted files", dest="Dpath",action="store")
result=parser.parse_args()

def extractFile(f,p,r):
	p=p.strip("\n")
	try:
		f.extractall(path=r,pwd=p)
		print 'Found password:' + p
	except:
		pass

def main():
	path = os.getcwd()
	fn= sys.argv[len(sys.argv) - 2]
	if result.Dpath != None:
		path = result.Dpath
	if zipfile.is_zipfile(fn):
		d = open (sys.argv[len(sys.argv) - 1], "r")
		zFile = zipfile.ZipFile(open (fn, "r"))
		for passwd in d.readlines():
			t = Thread(target=extractFile, args=(zFile, passwd,path))
			t.start()
		
	else:
		print "Error:"+ fn +" is not a zip file"

	
if __name__=="__main__":
	main()
