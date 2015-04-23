from __future__ import division
from numpy import *
from sklearn.tree import DecisionTreeClassifier
from math import *

def main():
	training_data = genfromtxt('training.txt', delimiter=1)
	X_train = training_data[:, :57]
	Y_train = training_data[:, 58]

	test_data = genfromtxt('test.txt', delimiter=1)
	X_test = test_data[:, :57]
	Y_test = test_data[:, 58]

	T = 1000
	D = ones(71) / 71
	clf = DecisionTreeClassifier(criterion="entropy", max_depth=1)

	for i in range(0, T):
		clf = clf.fit(X_train, Y_train, sample_weight=D)
		predicted_Y_train = clf.predict(X_train)
		#test_score = clf.score(X_test, Y_test)
		#print (1 - test_score)
		train_score = clf.score(X_train, Y_train, sample_weight=D)
		print (1 - train_score)

		et = 0

		for j in range(0,71):
			if not predicted_Y_train.item(j) == Y_train.item(j):
				et += D.item(j)

		at = 0.5 * log1p(1 / et - 1)

		norm_term = 0.0

		for j in range(0,71):
			yi = -1 if Y_train.item(j) == 0 else 1
			ht = -1 if predicted_Y_train.item(j) == 0 else 1
			D[j] = D.item(j) * exp(-1.0 * at * yi * ht)
			norm_term += D[j]

		D = D / norm_term

if __name__ == '__main__':
	main()