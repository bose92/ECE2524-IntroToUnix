#ECE 2524: Intro to Unix
#Homework 3 Problem 1
#Anamitra Bose

import fileinput
import sys
import argparse

parser = argparse.ArgumentParser(description='Integer processing.')
parser.add_argument('objects', nargs='*', type=str, default=sys.stdin)
parser.add_argument('--no-processes', action='store_true', dest='no-processes', help='Overlook blank lines')
parser.add_argument('--no-number-based', action='store_true', dest='no-number-based', help='Overlook non-number based lines')
args = parser.parse_args()

multiply = 1.0
if(len(sys.argv)>1):
	for pos in fileinput.input(args.files):
		if pos == '\n':
			if args.ignore_blank:
				continue
			else:
				print multiply
				multiply = 1.0
		elif len(pos) == 0:
			break
		else:
			try:
				multiply *= float(pos)
			except Exception as err:
				if args.ignore_non_numeric:
					continue
				else:
					sys.stderr.write(str(err))
					sys.exit(1)
else:
	while(1):
		pos = sys.stdin.readline()
		if pos == '\n':
			print multiply
			multiply = 1.0
		elif len(pos) == 0:
			break
		else:
			try:
				multiply *= float(pos)
			except Exception as err:
				sys.stderr.write(str(err))
				sys.exit(1)
print multiply
sys.exit(0)


