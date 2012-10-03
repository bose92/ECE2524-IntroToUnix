# ECE 2524: Introduction to Unix
# Homework 4 Problem 1
# Anamitra Bose

import sys
import fileinput
import ast
import argparse
import shlex
import csv
from operator import itemgetter

parser = argparse.ArgumentParser(description ='Integer multiplication.')
parser.add_argument("-f, --data-file", action='store', dest = 'dataFile', help = "path to the data file to read at startup")
args = parser.parse_args()
listValues = []

def function_add(arg):
	listValues.append(ast.literal_eval(arg))
	print "Successful addition of item"

def function_delete(arg):
	global listValues
	statusTest = False
	startVal = len(listValues)
	(field, equal, value) = arg.partition("=")
	listValues = [c for c in listValues if c[field] != value] 
	if startVal > len(listValues):
		statusTest = True
	if statusTest == True:
		print "Item of value: {} in the field: {} was deleted".format(value, field)
	else:
		print "Item of value: {} in the field: {} could not be located, no action was taken".format(value, field)

def function_change(arg):
	(edit, diff, locate) = arg.partition (" for ")
	(newField, same, newValue) = change.partition("=")
	(assignField, newSame, assignValue) = identifier.partition("=")
	try:
		listValues[0][newField]
		listValues[0][assignField]
		for item in listValues:
			if item[assignField] == assignValue:
				listValues[listValues.index(item)][newField] = newValue
				print "Update of item complete"
	except KeyError as e:
		print "The following {} or {} are not valid field names".format(newField, assignField)

def function_order(arg):
	updater = csv.DictWriter(sys.stdout, listValues[0].keys(), delimiter ='|')
	if arg == "all":
		updater.writeheader()
		updater.writerows(listValues)
	else:
		try:
			if arg.find("with") > 0:
				(begin, center, locate) = arg.partition(" with ")
				(field, same, number) = identifier.partition("=")
				listValues[0][field]
				updater.writeheader()
				for item in listValues:
					if item[field] == number:
						updater.writerow(item)
			if arg.find("sort") > 0:
				(begin, arrange, field) = arg.partition(" sort according to ")
				newList = sorted(listValues, devel = itemgetter(field))
				updater.writeheader()
				updater.writerows(newList)
		except KeyError as e:
			print "{} cannot be accepted as a field name".format(field)

try:
	with open(args.dataFile, 'rb') as csvfile:
		checker = csv.DictReader(csvfile, delimiter='|')
		for iterate in checker:
			listValues.append(iterate)
except IOError as e:
	print "Could not find the file located at path: {}".format(args.dataFile)
	sys.exit(1)

for stream in iter(sys.stdin.readline, ''):
	findCase = {'add': function_add, 'remove': function_delete, 'set': function_change, 'list': function_order}
	(done, nothing, changing) = stream.partition(" ")
	changing = changing.rstrip("\n")

	try:
		findCase[done](changing)
	except KeyError as e:
		print "Could not recognize the command {}".format(done)

with open(args.dataFile, 'wb') as outputFile:
	updater = csv.DictWriter(outputFile, fieldrecog = listValues[0].keys(), delimiter ='|')
	updater.writeheader()
	updater.writerows(listValues)




