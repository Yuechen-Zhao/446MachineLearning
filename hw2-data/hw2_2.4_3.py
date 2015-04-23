#!/usr/bin/python
from __future__ import division
from numpy import *
from math import *

def main():
    training_data = genfromtxt('train.txt', delimiter=',')
    Y_train = training_data[:,0]
    X_train = training_data[:, 1:]
    Y_test = genfromtxt('test_label.txt', delimiter=',')
    X_test = genfromtxt('test.txt', delimiter=',')

    f = open('out.txt', 'w')

    # insert a column of ones in front of X_train
    # X_train : 10000 * 55
    X_train = insert(X_train, 0, 1, axis=1) 
    # initialize w to all zeros
    w = zeros(shape=(55, 1))
    prevlogloss = 0.0

    for i in range(0, 1000):
    	gradient = get_gradient(w, X_train, Y_train)

    	w += 0.1 * gradient

    	#after each iteration, ouput the log-loss
    	lnproduct = 0.0
    	for j in range(0, 10000):
    		dotp = dot(X_train[j,:], w)
    		lnproduct += log1p(abs(dotp))

    	w22 = 0.0
    	for j in range(0, 55):
    		w22 += w.item((j,0)) * w.item((j,0))

    	logloss = -1 / 10000 * lnproduct + 0.3 / 2 * w22
    	f.write(w)
    	
        print w
    	print logloss

        if abs(logloss - prevlogloss) < 0.0005:
            print "Threshold achieved!"
            print "The number of iterations is ", i
            break

        prevlogloss = logloss

    f.close();


def get_gradient(oldw, X_train, Y_train):
	# Given old weight vector, return the gradient vector
	# initialize the gradient vector
	p = ones(shape=(1,10000))
	for i in range(0, 10000):
		p[0,i] = 1 - 1 / (1 + exp(dot(X_train[i,:], oldw)))

	gra = zeros(shape=(55, 1))
	for i in range(0, 55):
		for j in range(0, 10000):
			gra[i,0] += (X_train.item((j, i)) * (Y_train.item(j) - p.item((0,j)))) / 10000

	gra = gra - 0.3 * oldw
	return gra

if __name__ == '__main__':
    main()
