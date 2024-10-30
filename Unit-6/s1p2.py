'''
Problem 2: Find Frequency
Given the head of a linked list and a value val, return the frequency of val in the list. 
Evaluate the time and space complexity of your solution. 
Define your variables and provide a rationale for why you believe your solution has the stated 
time and space complexity.
'''
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def count_element(head, val):
	frequency = 0
	current = head
	while current:
		if current.value == val:
			frequency += 1
		current = current.next
	return frequency
	

head = Node(3, Node(1, Node(2, Node(1))))
val = 1
print(count_element(head, val))
#Example Usage:

# Input List: 3 -> 1 -> 2 -> 1
# Input: head = 3, val = 1
#Example Output:

# 2