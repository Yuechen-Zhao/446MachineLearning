#!/usr/bin/python
from __future__ import division
from numpy import *
from math import *

def main():

	# w : 55 * 1
	# Y_test : 1000 * 1
	# X_test : 1000 * 54

	w = genfromtxt('out.txt', delimiter=',')
	Y_test = genfromtxt('test_label.txt', delimiter=',')
	X_test = genfromtxt('test.txt', delimiter=',')

    # X_test : 1000 * 55

	X_test = insert(X_test, 0, 1, axis=1) 

	correct = 0
	predicttrue = 0
	predictfalse = 0
	for i in range(0, 1000):
		product = dot(X_test[i,:], w)
		if product > 0:
			predicttrue += 1
			if Y_test.item(i) == 1:
				correct += 1
		else:
			predictfalse += 1
			if Y_test.item(i) == 0:
				correct += 1

	print predicttrue
	print predictfalse
	print correct


if __name__ == '__main__':
	main()