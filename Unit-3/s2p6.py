'''
Problem 6: Sum Unique Elements
Write a function sum_of_unique_elements() that takes in two lists of integers, lst1 and lst2, as parameters 
and returns the sum of the elements that are unique in lst1.

An element is unique if:

it appears exactly once in lst1
it does not appear in lst2
'''
def sum_of_unique_elements(lst1, lst2):
	seen = {}
	total = 0
	if not lst1:
		return 0
	for num in lst1:
		if num in seen:
			seen[num]+=1
		if num not in seen and num not in lst2:
			seen[num]=1
		
	
	for key,value in seen.items():
		if value == 1:
			total += key
		
	return total
#Example Usage:

lstA = [1, 2 ,3, 4] 
lstB = [3, 4, 5, 6]
lstC = [7, 7, 7, 7]

sum1 = sum_of_unique_elements(lstA, lstB)
print(sum1)

sum2 = sum_of_unique_elements(lstC, lstB)
print(sum2)
#Example Output

#3
#0
