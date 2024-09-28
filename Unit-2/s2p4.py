'''
Problem 4:
Write a function that takes in a list of integers nums and counts the 
number of occurrences of each integer. The function returns the result 
as a dictionary with integers as keys and their counts as values.
'''
def count_occurrences(nums):
    count = {}
    for num in nums:
        if num not in count.keys():
            count[num]=1
        else:
            count[num]+=1
    return count
#Example Input: 
nums = [1, 2, 2, 3, 3, 3, 4]
print(count_occurrences(nums))
#Example Output: {1: 1, 2: 2, 3: 3, 4: 1}


