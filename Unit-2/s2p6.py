'''
Problem 6:
Write a function hasDuplicates() that takes in a list of integers nums 
and a positive number k as parameters. The function returns True if 
the list contains any duplicate elements within the range 0 to k (inclusive). 
If k is greater than the list's length, the solution should check for 
duplicates in the complete list. 
The function should return False otherwise.
'''
def hasDuplicates(nums, k):
	idx = {}
	for i in range(len(nums)):
		if nums[i] in idx:
			diff = i-idx[nums[i]]
			if diff < k:
				return True
		idx[nums[i]]= i
	return False
		
#Example Usage:

nums = [5, 6, 8, 2, 6, 4, 9]
check1 = hasDuplicates(nums, 3)
print(check1)
check2 = hasDuplicates(nums, 5)
print(check2)
#Example Output:

#False
#True