#! /bin/python
import argparse,pyPdf,sys
from pyPdf import PdfFileReader

parser = argparse.ArgumentParser()
parser.add_argument("file",help="Pdf file")
args=parser.parse_args()

def main():
	fileName= sys.argv[len(sys.argv)-1]
	pdfFile = PdfFileReader(file(fileName, 'rb'))
 	info = pdfFile.getDocumentInfo()
	print "The Metadata for the file" + fileName + " are: \n"
	for line in info:
		print line+ " : " +info[line]

if __name__== "__main__":
	main()
