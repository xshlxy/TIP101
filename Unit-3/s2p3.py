'''
Problem 3: Reverse Letters
Write a function reverse_only_letters() that takes in a string s as a parameter. 
The function reverses the order of the letters in the string and returns the new string. 
Non-letter characters should remain in their original positions.
'''
def reverse_only_letters(s):
    alp = []
    for char in s:
        if char.isalpha():
            alp.append(char)
    idx = len(alp)-1
    new_str = ""
    for char in s:
        if char.isalpha():
            new_str+=alp[idx]
            idx-=1
        else:
            new_str+=char

    return new_str
#Example Usage:

s = "a-bC-dEf-ghIj"
reversed_s = reverse_only_letters(s)
print(reversed_s)
#Example Output: j-Ih-gfE-dCba