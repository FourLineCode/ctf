#!/usr/bin/python3

with open('output.txt') as file:
	lines = file.readlines()

	for line in lines:
		print(chr(int(line.strip())), end="")