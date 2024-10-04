'''
Problem 2: Swap Ends
Write a function swap_ends() that accepts 
a string my_str as a parameter and 
returns a new string where the first 
and last characters from my_str 
are swapped.
'''
def swap_ends(my_str):
    new_str = ""
    for i in range(len(my_str)):
        if i == 0:
            new_str+=my_str[len(my_str)-1]
        elif i==(len(my_str)-1):
            new_str+=my_str[0]
        else:
            new_str+=my_str[i]
    return new_str

#Example Usage:

my_str = "boat"
swapped = swap_ends(my_str)
print(swapped)
#Example Output: toab