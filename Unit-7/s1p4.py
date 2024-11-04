'''
Problem 4: Recursive Power of 2
Given an integer n, return True if n is a power of two. Otherwise, return `False``.

An integer n is a power of two if there exists an integer x such that n == 2ˣ.

Solve the problem recursively. What is the time complexity of this function?
What is the space complexity?
'''
def is_power_of_two(n):
	if n == 1:
		return True
	elif n == 2:
		return True
	elif n <= 0 or n%2!=0:
		return False
	return is_power_of_two(n//2)  
	
print(is_power_of_two(5))		