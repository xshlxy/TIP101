'''
Problem 5:
Write a function find_majority_element() that takes in a list of integers 
elements and finds the majority element in the list. A majority element 
is an element that appears more than n/2 times where n is the size of the 
list. If there is no majority element, return None.
'''#
def find_majority_element(elements):
    count = {}
    for num in elements:
        if num not in count.keys():
            count[num]=1
        else:
            count[num]+=1
    for key,value in count.items():
        if value > len(count)/2:
            return key
    return None
#Example Usage:

elements = [2, 2, 1, 1, 1, 2, 2]
print(find_majority_element(elements))
#Example Output: 2