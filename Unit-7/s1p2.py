'''
Problem 2: Factorial Cases
Given the base case and recursive case, write a function factorial() 
that returns the factorial of a non-negative integer n. 
The factorial of a number is the product of all numbers between 1 and n.

Base Case: The smallest number we can find a factorial of is 0. 
By definition, the factorial of 0 is 1.

Recursive Case: We can restate the problem to say that the 
factorial of n is n * the factorial of n-1.
'''
def factorial(n):
	if n == 0 or n==1:
		return 1
	return n * factorial(n-1)
#Example Usage:
print(factorial(5))
# Example Input: 5
#Example Output:

# Expected Output: 120
# Explanation: 5! = 5 * 4 * 3 * 2 * 1 = 120