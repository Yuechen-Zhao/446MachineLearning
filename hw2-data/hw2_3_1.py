#!/usr/bin/python
from __future__ import division
from numpy import *
from math import *

def main():
	training_data = genfromtxt('oversampled_train.txt', delimiter=',')

	# X_train : 17729 * 54
	# Y_train : 17729 * 1
	Y_train = training_data[:,0]
	X_train = training_data[:, 1:]
	Y_test = genfromtxt('test_label.txt', delimiter=',')
	X_test = genfromtxt('test.txt', delimiter=',')
	# X_test : 1000 * 55
	X_test = insert(X_test, 0, 1, axis=1) 

	# insert a column of ones in front of X_train
    # X_train : 17729 * 55
	X_train = insert(X_train, 0, 1, axis=1)
	# initialize w to all zeros
	# w : 55 * 1
	w = zeros(shape=(55, 1))
	for t in range(0, 1000):

		for i in range(0, 17729):
			val = dot(X_train[i,:], w)
			sign = 1 if val > 0 else 0

			if sign != Y_train.item(i):
				for j in range(0, 55):
					yi = 1 if Y_train.item(i) == 1 else -1
					w[j,0] += yi * X_train[i,j]

		
		truepos = 0
		precisionmu = 0
		recallmu = 0

		trueneg = 0
		precisionmu2 = 0
		recallmu2 = 0

		maxsum = 0

		for i in range(0, 1000):
			product = dot(X_test[i,:], w)
			if product > 0: # predict CLICK
				precisionmu += 1
				if Y_test.item(i) == 1: # true positive
					recallmu += 1
					truepos += 1
				else:
					recallmu2 += 1
			else: # predict NO CLICK
				precisionmu2 += 1
				if Y_test.item(i) == 1: # but actually CLICK
					recallmu += 1
				else:
					trueneg += 1
					recallmu2 += 1
		
		print "1 CLASS : precision =", (truepos / precisionmu)
		print "1 CLASS : recall =", (truepos / recallmu)
		print "0 CLASS : precision =", (trueneg / precisionmu2)
		print "0 CLASS : recall =", (trueneg / recallmu2)

		if truepos / recallmu + trueneg / recallmu2 > 1.02:
			break

if __name__ == '__main__':
	main()
