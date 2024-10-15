'''
Problem 1: Prime Number
Write a function is_prime() that takes in a positive 
integer n and returns True if it is a prime number and 
False otherwise. A prime number is a number greater 
than 1 that has no positive divisors other than 1 and 
itself.
'''
def is_prime(n):
    divisor = 1
    if n <= 1:
        return False
    if n%2 == 0 or n%3 == 0:
        return False
    for num in range(1,n):
        if n%num == 0:
            divisor += 1
        if divisor > 2:
            return False
    return True
#Example Usage:

print(is_prime(5))
print(is_prime(12))
print(is_prime(9))
#Example Output:

#True
#False
#False