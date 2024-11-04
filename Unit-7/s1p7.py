'''
Problem 7: Find Floor
Given a sorted list of integers and a value x, return the index of the floor of x. 
The floor of x is the largest element in the array smaller than or equal to x. 
If there is no floor of x, return -1.

Evaluate the time and space complexity of your function.
'''
def find_floor(lst, x):
	i=0
	if lst[0] > x and i==0:
		return -1
	elif lst[i] < x:
		i+=1
		return find_floor(lst[i:], x)
	else:
		return (i - 1)  


#Example Usage:

lst = [1, 2, 8, 10, 11, 12, 19] 
x = 5
print(find_floor(lst, x))
#Example Output:

# Expected Output: 1
# 2 is the largest element in the list that is less than or equal to 5. 2 has index 1 in the list.