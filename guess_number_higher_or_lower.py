# this is a binary search problem 
# easy
import math

def binary_serach(n):
	# first create the ordered list from 1 to n
	arr = list(range(1, n+1))
	print(arr)
	# if n == 1:
	# 	arr = [1]
	# 	arr += list(range(1, n))
	# 	print('from above', arr)
	# else:
	# 	arr = list(range(1, n))
	# 	print('from below', arr)
	low = 0
	high = len(arr) - 1

	while low <= high:
		middle = math.floor((low + high) / 2)
		guessed_number = arr[middle]

        # guess is a pre defined function in the leetcode site 
        # it guesses a number randomly from 1 to n
        # and returns 0 if equals your guess
        # -1 if your guess is higher that the choosen number 
        # and 1 otherwise
        # define a function that does the same job explained above
        # call it guess() and you're all done
		# guess_api_result = guess(guessed_number)
        

		# uncomment this 
		# if guess_api_result == 0:
  #           # found it 
		# 	return guessed_number
		# elif guess_api_result == -1:
		# 	high = middle - 1
		# else:
		# 	low = middle + 1

binary_serach(2)