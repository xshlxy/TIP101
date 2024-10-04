'''
Problem 3: Is Pangram
Write a function is_pangram() that takes in a string my_str as a parameter 
and returns True if the string is a pangram and False if not. A pangram is a 
sentence containing every letter in the English alphabet.
'''
def is_pangram(my_str):
    seen = []
    for char in my_str:
        if char not in seen:
            seen.append(char)
    if len(seen) >= 26:
        return True
    else:
        return False
#Example Usage:

my_str = "The quick brown fox jumps over the lazy dog"
print(is_pangram(my_str))

str2 = "The dog jumped"
print(is_pangram(str2))
#Example Output:

#True
#False