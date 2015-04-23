#!/usr/bin/python
from __future__ import division
from numpy import *
from math import *

def main():

	# w : 55 * 1

	w = genfromtxt('output.txt', delimiter=',')
	normsqr = 0
	for i in range(1,55):
		normsqr += w.item(i) * w.item(i)

	l2 = sqrt(normsqr)
	print l2

if __name__ == '__main__':
	main()