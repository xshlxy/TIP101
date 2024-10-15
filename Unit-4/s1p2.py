'''
Problem 2: Two-Pointer Reverse List
Write a function reverse_list() that takes in a list 
lst and returns elements of the list in reverse order. 
The list should be reversed in-place without using 
list slicing (e.g. lst[::-1]).
'''
def reverse_list(lst):
    pointer1 = 0
    pointer2 = len(lst)-1
    while pointer1 < pointer2:
        temp = lst[pointer1]
        lst[pointer1]=lst[pointer2]
        lst[pointer2]=temp
        pointer1+=1
        pointer2-=1
    
    return lst
lst = [1,2,3,4,5]
print(reverse_list(lst))
#Example Output: [5, 4, 3, 2, 1]