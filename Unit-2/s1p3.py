'''
Problem 3:
Write a function print_pair() that takes in a dictionary dictionary and a key target as parameters. 
The function looks for the target and when found, it prints the key and it's associated value as 
"Key: <key>" followed by "Value: <value>". 
If target is not in dictionary, print "That pair does not exist!".
'''
def print_pair(dictionary, target):
    if target in dictionary:
        print("Key:" + target)
        print("Value:" + dictionary[target])
    else:
        print("That pair does not exist!")
#Example Usage:

dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
print_pair(dictionary, "patrick")
print_pair(dictionary, "plankton")
print_pair(dictionary, "spongebob")
#Example Output:
'''
Key: patrick
Value: star
That pair does not exist!
Key: spongebob
Value: squarepants
'''