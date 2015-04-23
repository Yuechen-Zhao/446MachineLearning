from numpy import *

def main():

	# create array 0...70, 71 rows in total
	arr = array([[0,0]])
	for i in range(1, 71):
		arr = concatenate((arr, array([[i,i]])), axis=0)
	
	total = 0
	# 100 iterations
	for i in range(0, 100):
		temparr = array([[100,100]])
		count = 0

		for j in range(0, 71):
			random.shuffle(arr)

			if arr.item((0,0)) in temparr[:,0]:
				count += 1
			
			temparr = concatenate((temparr, arr[:1,:]), axis=0)
			
		total += 1.0 * (71 - count) / 71

	print total / 100.0


if __name__ == '__main__':
	main()