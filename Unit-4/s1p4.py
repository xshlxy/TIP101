'''
Problem 4: Move Even Integers
Write a function sort_list_by_parity() that takes 
in an integer list nums as a parameter and moves 
all the even integers at the beginning of the list 
followed by all the odd integers. The function 
returns any list that satisfies this condition.
'''
def sort_array_by_parity(nums):
    pointer1 = 0
    pointer2 = 1
    while pointer1 <= pointer2:
        if nums[pointer1]%2==0:
            pointer1+=1
            pointer2+=1
        else:
            temp = nums[pointer1]
            nums[pointer1]=nums[pointer2]
            nums[pointer2]=temp
    
    return nums

#Example Usage:

nums = [3,1,2,4]
nums2 = [0]
print(sort_array_by_parity(nums))
print(sort_array_by_parity(nums2))
#Example Output:

#[2,4,3,1]
# Additional acceptable outputs are [4,2,3,1], [2,4,1,3], and [4,2,1,3]
#[0]