# ECE 2524 Homework 2 Problem 3 Anamitra Bose
import string
from sys import argv
script, nameOfFile = argv
workLocation = open(nameOfFile)
print "ACCOUNT SUMMARY"
total = 0 
iterate = 0
next = 0
low = 50
high = 0
for line in workLocation.readlines():
	values = line.split()
	iterate = iterate + 1
	next = float(values[2])
	total = total + float(values[2])
	if next > high:
		high = next
		newHighName = values[1]
	if next < low:
		low = next
		newLowName = values [1]
print "Total amount owed =", total
print "Average amount owed=", (total/iterate)
print "Maximum amount owed =", high, "by", newHighName
print "Minimum amount owed =", low, "by", newLowName
