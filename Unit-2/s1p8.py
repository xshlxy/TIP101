'''
Problem 8:
Write a function index_to_value_map() that takes in a list lst and returns a dictionary that 
maps the index of each element in lst to its value.
'''
def index_to_value_map(lst):
    dictionary = dict()
    current_idx = 0
    for value in lst:
      dictionary[current_idx]=value
      current_idx+=1  
    return dictionary
#Example Input: 
lst = ["apple", "banana", "cherry"]
print(index_to_value_map(lst))
#Example Output: {0: "apple", 1: "banana", 2: "cherry"}