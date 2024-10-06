'''
Problem 2: Remove Duplicates
Write a function remove_duplicates() that takes in a sorted list of integers nums as a parameter and removes all duplicates in the list. 
The function returns the modified list.
'''
def remove_duplicates(nums):
    if nums == []:
        return 0
    seen = []
    i=0
    while i < len((nums)):
        if nums[i] not in seen:
            seen.append(nums[i])
            i += 1
        else:
            nums.remove(nums[i])
    return nums
#Example Input: 
nums = [1,1,1,2,3,4,4,5,6,6]
print(remove_duplicates(nums))
#Example Output: no_dups = [1,2,3,4,5,6]

