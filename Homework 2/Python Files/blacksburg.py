 # ECE 2524 Homework 2 Problem 2 Anamitra Bose
import string
from sys import argv
script, nameOfFile = argv
workLocation = open(nameOfFile)
stringFormat = ', '
print "ACCOUNT INFORMATION FOR BLACKSBURG RESIDENTS"
for line in workLocation.readlines():
	values = line.split()
	if values[3] == 'Blacksburg':
		displayFormat = (values[4], values[1], values[0], values[2])
		print stringFormat.join(displayFormat)
