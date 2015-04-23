from __future__ import division
from numpy import *
from sklearn.tree import DecisionTreeClassifier

def main():
	training_data = genfromtxt('training.txt', delimiter=1)
	test_data = genfromtxt('test.txt', delimiter=1)
	X_test = test_data[:, :57]
	Y_test = test_data[:, 58]

	# get the first predicted_Y_test
	random.shuffle(training_data)
	trainappend_data = training_data[:1, :]
	for j in range(0, 49):
		random.shuffle(training_data)
		trainappend_data = concatenate((trainappend_data, training_data[:1, :]), axis=0)
	clf = DecisionTreeClassifier(criterion="entropy", max_depth=2)
	clf = clf.fit(trainappend_data[:, :57], trainappend_data[:, 58])
	predicted_Y_test = clf.predict(X_test)
	accuracy = getaccuracy(Y_test, predicted_Y_test, 1)
	#print len(trainappend_data)
	#print predicted_Y_test
	print (1-accuracy)

	for i in range(2, 101):
		random.shuffle(training_data)
		trainappend_data2 = training_data[:1, :]
		for j in range(0, 49):
			random.shuffle(training_data)
			trainappend_data2 = concatenate((trainappend_data2, training_data[:1, :]), axis=0)
		clf = clf.fit(trainappend_data2[:, :57], trainappend_data2[:, 58])
		
		predicted_Y_test = predicted_Y_test + clf.predict(X_test)
		accuracy = getaccuracy(Y_test, predicted_Y_test, i)
		#print len(trainappend_data2)
		#print predicted_Y_test
		print (1-accuracy)

def getaccuracy(Y_test, predicted_Y_test, div):
	count = 0
	for i in range(0, 35):
		if Y_test.item(i) == 0 and predicted_Y_test.item(i) / div <= 0.5:
			count += 1
		elif Y_test.item(i) == 1 and predicted_Y_test.item(i) / div > 0.5:
			count += 1

	return count/35

if __name__ == '__main__':
	main()