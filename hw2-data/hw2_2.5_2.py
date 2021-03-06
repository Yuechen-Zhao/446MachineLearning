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

    #f = open('out.txt', 'w')

    # insert a column of ones in front of X_train
    # X_train : 17729 * 55
    X_train = insert(X_train, 0, 1, axis=1) 
    # initialize w to all zeros
    w = zeros(shape=(55, 1))
    for i in range(0, 5000):
    	gradient = get_gradient(w, X_train, Y_train)

    	w += 0.01 * gradient

    	#after each iteration, ouput the log-loss
    	lnproduct = 0.0
    	for j in range(0, 17729):
    		dotp = dot(X_train[j,:], w)
    		lnproduct += log1p(abs(dotp))

    	w22 = 0.0
    	for j in range(0, 55):
    		w22 += w.item((j,0)) * w.item((j,0))

    	logloss = -1 / 17729 * lnproduct + 0.3 / 2 * w22
    	#f.write(w)

    	print w
    	print "i =", i
    	print "logloss =", logloss

    f.close();


def get_gradient(oldw, X_train, Y_train):
	# Given old weight vector, return the gradient vector
	# initialize the gradient vector
	p = ones(shape=(1,17729))
	for i in range(0, 17729):
		p[0,i] = 1 - 1 / (1 + exp(dot(X_train[i,:], oldw)))

	gra = zeros(shape=(55, 1))
	for i in range(0, 55):
		for j in range(0, 17729):
			gra[i,0] += (X_train.item((j, i)) * (Y_train.item(j) - p.item((0,j)))) / 17729

	gra = gra - 0.3 * oldw
	return gra

if __name__ == '__main__':
    main()
