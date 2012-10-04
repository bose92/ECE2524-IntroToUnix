#ECE 2524: Intro to Unix
#Homework 3 Problem 1
#Anamitra Bose

import argparse
import sys

parser = argparse.ArgumentParser(description='Integer processing.')
args = parser.parse_args()

multiply = 1.0
while (1):
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

