'''
Problem 1:
Write a function is_subsequence() that takes in a list of integers lst and a list of integers sequence as parameters. 
Given these two lists, determine whether the sequence list is a subsequence of the lst list. 
A subsequence of a list is a set of numbers that aren't necessarily adjacent but are in the same 
relative order as they appear in the list. 
Return True if sequence is a subsequence, and False otherwise.
'''
def is_subsequence(lst, sequence):
    seq_idx=0
    for num in lst:
        if seq_idx == len(sequence):
            return True
        if sequence[seq_idx]==num:
            seq_idx += 1
    return seq_idx == len(sequence)

#Example Usage:

lst = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(is_subsequence(lst, sequence))


#Example Output: True













