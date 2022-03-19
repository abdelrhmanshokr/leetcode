# this is a binary search problem
# easy
import math

def search(arr, number_to_be_found):
	# initializing start(low), end(high)
	low = 0
	high = len(arr) - 1

	# applying the binary search algorithm 
	while low <= high:
		middle = math.floor((high + low) / 2) # middle item in arr
		guess = arr[middle]

		if guess == number_to_be_found:
			# number is found in the middle of the array
			return middle
		elif guess < number_to_be_found:
			# update low = the item to the right to the middle
			low = middle + 1
		else:
			# the final posibility is the guess > number to be found
			# then update high = the number to the left of the middle
			high = middle - 1 

	# then it's not found
	# then return where to insert it so the array will remain ordered

	return low 

arr = [1, 2, 3, 4, 5, 6, 10]
print(search(arr, 7))