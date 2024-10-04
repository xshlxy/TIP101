'''
Problem 5: First Unique
Write a function first_unique_char() that given a string my_str as a parameter, 
it finds the first non-repeating character in it and returns its index. 
If it does not exist, then return -1.
'''
def first_unique_char(my_str):
    seen = {}
    for char in my_str:
        if my_str.count(char) == 1:
            return my_str.find(char)
    return -1
            
        
    
#Example Usage:

my_str = "leetcode"
print(first_unique_char(my_str))

str2 = "loveleetcode"
print(first_unique_char(str2))

str3 = "aabb"
print(first_unique_char(str3))
#Example Output

#0
#2
#-1