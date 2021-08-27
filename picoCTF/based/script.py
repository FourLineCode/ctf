#!/usr/bin/python3

import sys

string = sys.argv[1]
l = string.split()


s = ''
for i in l:
	# convert octal to text
	s += chr(int(i, 8))

print(s)