'''
Problem 1: Sum of Strings
Write a function sum_of_number_strings() that takes in a list of strings nums. 
Each string is a representations of integers. 
The function should return the sum of these strings as an integer.
'''
def sum_of_number_strings(nums):
    total = 0
    for num in nums:
        total+=int(num)
    return total
#Example Usage:

nums = ["10", "20", "30"]
sum = sum_of_number_strings(nums)
print(sum)
#Example Output: 60