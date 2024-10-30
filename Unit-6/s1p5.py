'''
Problem 5: Is Palindrome?
Given the head of a singly linked list, return True if the values of the linked list are palindromic and False otherwise. 
Use the two-pointer technique in your solution.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you 
believe your solution has the stated time and space complexity.
'''
class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def is_palindrome(head):
    slow, fast = head, head.next
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    
    pre, cur = None, slow.next
    while cur:
        t = cur.next
        cur.next = pre
        pre, cur = cur, t
    
    while pre:
        if pre.value != head.value:
            return False
        pre, head = pre.next, head.next
    return True
#Example Usage:

head = Node(1, Node(2, Node(2)))
print(is_palindrome(head))
# Input List:
# 1 -> 2 -> 1
# Input: head = 1
#Example Output:

# True