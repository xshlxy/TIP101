'''
Problem 4: Reverse String
Write a function reverse_string() that takes a string my_str as a parameter 
and returns the string reversed.
'''
def reverse_string(my_str):
    new_str = ""
    last_idx = len(my_str)-1
    for i in range(len(my_str)):
        new_str+=my_str[last_idx]
        last_idx-=1
    return new_str
#Example Usage:

my_str = "live"
print(reverse_string(my_str))
#Example Output: evil