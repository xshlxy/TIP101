'''
Problem 1: Long Pressed
Write a function is_long_pressed() that takes in a 
string name and a string typed as parameters. 
Imagine your friend is typing their name into 
a keyboard and when typing a character, 
the key might get long pressed and the character 
will be typed 1 or more times.

The function should examine the typed characters 
and return True if it is possible that it was your 
friends name with some characters being long 
pressed and False otherwise.
'''
def is_long_pressed(name, typed):
    pass
#Example Usage:

name = "alex"
typed = "aaleex"
print(is_long_pressed(name, typed))

name2 = "saeed"
typed2 = "ssaaedd"
print(is_long_pressed(name2, typed2))

name3 = "courtney"
typed3 = "courtney"
print(is_long_pressed(name3, typed3))
#Example Output:

# 'a' and 'e' were long pressed in "alex"
#True
# there are two 'e's in "saeed", and only one 'e' in the typed string 
#False
# equal strings are considered long pressed
#True