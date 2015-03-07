import re, sys


readfile = raw_input("Enter file name/location: ")
regex = re.compile( raw_input('Enter regex pattern: ') )

try:
	file_read = open(readfile,'r')
except:
	print("Couldn't find that file!")
	sys.exit()

with open("matches.txt","w") as output:
	matches = re.findall(regex, file_read.read())
	output.write('\n'.join(matches))

	print("Found "+str(len(matches))+" matches.")
