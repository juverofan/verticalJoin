#Merge 2 files with same lines into 1 files

from os import listdir
from os.path import isfile, join
import os
import sys
import argparse

text = 'The Vertical Join script for join 2 same-line files vertically.'
parser = argparse.ArgumentParser(description = text)  

parser.add_argument("-f", "--filex", help="The file A")
parser.add_argument("-j", "--joint", help="the joined file")
parser.add_argument("-o", "--output", help="The output file")
args = parser.parse_args()

filex = args.filex

if args.joint:
	part = args.joint
else:
	part = "partition.txt"

if args.output:
	output = args.output
else:
	output = 'output'

def readLine(files,linen):
	fp = open(files,"r")
	for i, line in enumerate(fp):
		if i == (linen-1):
			return line.strip()
		elif i > (linen-1):
			break
	fp.close()

def countLines(files):
	with open(files) as f:
		return len(f.readlines())

print("Line number: "+str(countLines(filex))+" - "+str(countLines(part))+"\n")
if countLines(filex) == countLines(part):
	rOut = open(output,"w")
	rline = open(filex,"r")	
	i = 1
	for l in rline:
		#print(str(readLine(part,i)))
		rOut.write(str(l).rstrip("\n")+str(readLine(part,i)).strip()+"\n")
		i=i+1
	rOut.close()
else:
	print("Two files're not same lines.")		
