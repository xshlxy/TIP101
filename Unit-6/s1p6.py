'''
Problem 6: Put it in Reverse
Given the head of a singly linked list, reverse the list, and return the reversed list. You must reverse the list in place. Return the head of the reversed list.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
'''
class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def reverse(head):
    slow = None
    fast = head
    while fast:  
        node_next = fast.next
        
        fast.next = slow
        slow = fast
            
        fast = node_next
    return slow.value
#Example Usage:

head = Node(1, Node(2, Node(3, Node(4))))
print(reverse(head))
# Input List: 1 -> 2 -> 3 -> 4
# Input: head = 1
#Example Output:

# Expected Return Value: 4
# Expected Result List: 4 -> 3 -> 2 -> 1