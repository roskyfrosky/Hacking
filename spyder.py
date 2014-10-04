#! /bin/python
from bs4 import BeautifulSoup
import urllib2,urllib,sys,argparse
parser =argparse.ArgumentParser()
parser.add_argument("url", help="Input the url to Spyder")
parser.add_argument("-o","--output",help="Output the result to a file", action="store",dest="out")
parser.add_argument("-d","--depth",help="depth of spyder",action="store", dest="depth")
args=parser.parse_args()
#Default Depth --> 1
def search(d):
	try:
		content= urllib2.urlopen(d).read()
		soup= BeautifulSoup(content)
		for link in soup.find_all('a',href=True): 
			if "http://" in link['href']:
				aux1.append("\n"+ link['href']+"\n")  
		else:  	
			string= d+ "/"+link['href'] +"\n"
		    	aux1.append(string)
	except:
		pass
       
def main():
    global f ,aux , aux1
    j =1   
    url=sys.argv[len(sys.argv)-1] #url start
    aux,aux1,final=[],[],[] # aux list
    aux.append(url)
    if args.depth != None:
        j = int(args.depth)
    #Start the spyder           
    while j > 0 :   
        j-=1
        while aux:
		url1 = aux.pop(0)
		final.append(url1)
		search(url1)
	for i in aux1:
		if i==None :
		    aux1.remove(i)
	aux.extend(aux1) 
	final.extend(aux1)
	del aux1[:] 
    if args.out!=None :
        f=open(args.out,"w")
        for line in final:
            f.write(line)
        f.close()
    else:
        for line in final:
            print line
           
if __name__=="__main__":
    main()
