# ECE 2524 Homework 2 Problem 1 Anamitra Bose
import string
with open('/etc/passwd','r') as f:
	for line in f:
		var = string.splitfields(line,':')
		print "%s %s" % (str(var[0]).ljust(10), str(var[6]).rstrip('\n'))

