#!/usr/bin/python
from __future__ import division
from numpy import *
from math import *

def main():

	# w : 55 * 1
	# Y_test : 1000 * 1
	# X_test : 1000 * 54

	w = genfromtxt('output.txt', delimiter=',')
	Y_test = genfromtxt('test_label.txt', delimiter=',')
	X_test = genfromtxt('test.txt', delimiter=',')

    # X_test : 1000 * 55

	X_test = insert(X_test, 0, 1, axis=1) 

	# truepos = 0
	# precisionmu = 0
	# recallmu = 0
	# for i in range(0, 1000):
	# 	product = dot(X_test[i,:], w)
	# 	if product > 0: # predict CLICK
	# 		precisionmu += 1
	# 		if Y_test.item(i) == 1: # true positive
	# 			recallmu += 1
	# 			truepos += 1
	# 	elif Y_test.item(i) == 1: # predict NO CLICK, but actually CLICK
	# 		recallmu += 1
				

	# print "truepos =", truepos
	# print "precisionmu = ", precisionmu
	
	# print "recallmu =", recallmu

	trueneg = 0
	precisionmu = 0
	recallmu = 0
	for i in range(0,1000):
		product = dot(X_test[i,:], w)
		if product <= 0:
			precisionmu += 1
			if Y_test.item(i) == 0:
				recallmu += 1
				trueneg += 1
		elif Y_test.item(i) == 0:
			recallmu += 1

	print "trueneg =", trueneg
	print "precisionmu =", precisionmu
	print "recallmu =", recallmu


if __name__ == '__main__':
	main()