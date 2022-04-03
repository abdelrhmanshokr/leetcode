# this is a binary search problem
# easy
import math

def binary_search(arr, target):
	low = 0
	high = len(arr) - 1

	while low <= high:
		middle = math.floor((high + low) / 2)
		guess = arr[middle]

		if guess == target:
			return middle
		elif target > guess:
			low = middle + 1 
		else: 
			high = middle - 1 

	return -1

arr = [-1,0,3,5,9,12]
print(binary_search(arr, 9))