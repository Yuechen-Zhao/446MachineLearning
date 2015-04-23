from __future__ import division
from numpy import *
from math import *
from random import randint

def main():

	# X = 1000 * 157
	# Y = 1000 * 1
	X = genfromtxt('digit.txt')
	Y = genfromtxt('labels.txt', dtype=int)

	for k in range(1, 11):

		# initialize random centers
		centers = zeros(shape=(k, 157))
		for i in range(0, k):
			randomnumber = randint(0, 999)
			centers[i,:] = X[randomnumber, :]

		assignment = [0] * 1000

		for iter in range(0, 20):

			# assign each point to a new cluster
			updatecenter = 0
			for i in range(0, 1000): # each point
				dist = float("inf")
				for j in range(0, k): # each center
					newdist = linalg.norm(X[i,:] - centers[j,:])
					if (newdist < dist):
						updatecenter += 1
						dist = newdist
						assignment[i] = j

			# re-calculate the centers
			for i in range(0, k): # each cluster
				newcenter = zeros(shape=(1, 157))
				count = 0 # how many points added?

				for j in range(0, 1000):
					if assignment[j] == i: # for each point, if the point in this cluster, add into newcenter
						count += 1
						newcenter += X[j,:]

				if count > 0:
					newcenter *= 1.0 / count
					centers[i,:] = newcenter

			# if never updated assignment
			if updatecenter == 0:
				print iter
				break

		# calculate within group sum of squares
		sumss = 0.0
		for i in range(0, k):
			for j in range(0, 1000):
				if assignment[j] == i:
					sumss += pow(linalg.norm(X[j,:] - centers[i,:]), 2)

		# mistake rate
		mistakes = 0
		for i in range(0, k):

			one = 0
			three = 0
			five = 0
			seven = 0

			for j in range(0, 1000):
				if assignment[j] == i:
					if Y[j] == 1:
						one += 1
					elif Y[j] == 3:
						three += 1
					elif Y[j] == 5:
						five += 1
					else:
						seven += 1

			if one >= three and one >= five and one >= seven:
				mistakes += three + five + seven
			elif three >= one and three >= five and three >= seven:
				mistakes += one + five + seven
			elif five >= one and five >= three and five >= seven:
				mistakes += one + three + seven
			else:
				mistakes += one + three + five
		
		print (1.0 * mistakes / 1000)
		# print sumss

if __name__ == '__main__':
		main()