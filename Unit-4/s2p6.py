'''
Problem 6: Duplicates Within Range
Write a function contains_nearby_duplicate() that 
takes in a list lst and a positive number k as 
parameters. The function returns True if the list 
contains any duplicate elements within the range k 
and False otherwise. If k is more than the list's 
size, the solution should check for duplicates in 
the complete list.
'''
def contains_nearby_duplicate(lst, k):
    pass
#Example Usage:

lst = [1, 2, 3, 1, 2, 3]
lst2 = [1, 0, 1, 1]
print(contains_nearby_duplicate(lst, 2))
print(contains_nearby_duplicate(lst2, 1))
#Example Output:

#False
#True
