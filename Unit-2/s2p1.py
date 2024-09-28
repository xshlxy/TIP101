'''
Problem 9:
Write a function cast_vote() that records a vote for a candidate in an election. The function accepts a dictionary votes that maps candidates to their current number of votes and a string candidate that represents the candidate the user would like to vote for. If the candidate doesn't exist, add them to the dictionary. The function should return the updated dictionary.
'''
def cast_vote(votes, candidate):
    pass
#Example Usage:

votes = {"Alice": 5, "Bob": 3}
cast_vote(votes, "Alice")
print(votes)
cast_vote(votes, "Gina")
print(votes)
#Example Output:

#{"Alice": 6, "Bob": 3}
#{"Alice": 6, "Bob": 3, "Gina": 1}

'''
Problem 10:
Write a function that takes in two dictionaries, dict1 and dict2 and finds all keys common to both dictionaries. The function returns a list of common keys.
'''
def common_keys(dict1, dict2):
	pass
#Example Usage:

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
common_list = common_keys(dict1, dict2)
print(common_list)
#Example Output:

#['b', 'c']

'''
Problem 11:
Given a dictionary tasks where keys are task names and values are priorities (1-10, where 10 is the highest priority), write a function get_highest_priority_task() that removes the task with the highest priority from the dictionary and returns its name.
If two tasks have the same priority, return the task that comes first in the alphabet.
'''
def get_highest_priority_task(tasks):
	pass
#Example Usage:

tasks = {"task1": 8, "task2": 10, "task3": 9, "task4": 10, "task5": 7}
perform_task = (get_highest_priority_task(tasks))
print(perform_task)

perform_task = (get_highest_priority_task(tasks))
print(perform_task)

perform_task = (get_highest_priority_task(tasks))
print(perform_task)

print(tasks)
#Example Output:
'''
task2
task4
task3
{"task1": 8, "task5": 7}
'''

'''
Problem 12:
Write a function that takes in a list of integers nums and counts the number of occurrences of each integer. The function returns the result as a dictionary with integers as keys and their counts as values.
'''
def count_occurrences(nums):
    pass
#Example Input: 
nums = [1, 2, 2, 3, 3, 3, 4]
#Example Output: {1: 1, 2: 2, 3: 3, 4: 1}

'''
Problem 13:
Write a function find_majority_element() that takes in a list of integers elements and finds the majority element in the list. A majority element is an element that appears more than n/2 times where n is the size of the list. If there is no majority element, return None.
'''#
def find_majority_element(elements):
    pass
#Example Usage:

elements = [2, 2, 1, 1, 1, 2, 2]
print(find_majority_element(elements))
#Example Output: 2

'''
Problem 14:
Write a function hasDuplicates() that takes in a list of integers nums and a positive number k as parameters. The function returns True if the list contains any duplicate elements within the range 0 to k (inclusive). If k is greater than the list's length, the solution should check for duplicates in the complete list. The function should return False otherwise.
'''
def hasDuplicates(nums, k):
	pass
#Example Usage:

nums = [5, 6, 8, 2, 6, 4, 9]
check1 = hasDuplicates(nums, 3)
print(check1)
check2 = hasDuplicates(nums, 5)
print(check2)
#Example Output:

#False
#True

'''
Problem 15:
Write a function divideList() that takes in an integer list nums consisting of 2*n integers as parameters. The function divides nums into n pairs such that:

Each element belongs to exactly one pair
The elements present in a pair are equal
Return True if nums can be divided into n pairs, otherwise return False.
'''
def divideList(nums):
    pass
#Example Input: 
nums = [3,2,3,2,2,2]
#Example Output: True
#Explanation: There are 6 elements in nums, so they should be divided into 6 / 2 = 3 pairs. If nums is divided into the pairs (2, 2), (3, 3), and (2, 2), it will satisfy all the conditions.

#Example Input: nums = [1,2,3,4]
#Example Output: False
#Explanation: There is no way to divide nums into 4 / 2 = 2 pairs such that the pairs satisfy every condition.