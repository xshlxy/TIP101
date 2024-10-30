'''
Problem 4: Convert Binary Number in a Linked List to Integer
You are given the head of a linked list. Each value in the linked list is either 0 or 1, 
and the entire linked list represents a binary number. 
Return an integer that is the decimal value of the number represented by the linked list. 
The most significant bit is at the head of the linked list.
'''
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def binary_to_int(head):
	pass
#Example Usage:

# 1 -> 0 -> 1
num1 = 1
num2 = 0
num3 = 1
int_num = binary_to_int(num1)
# 101 in binary 

print(int_num)
#Example Output: 5