'''
Problem 4:
Write a function keys_v_values() that takes in a dictionary dictionary whose keys and values are both integers. 
The function should find the sum of all keys in the dictionary and the sum of all values.
If the sum of all keys is greater than the sum of all values, the function should return the string "keys".
If the sum of all values is greater than the sum of all keys, the function should return the string "values".
If keys and values have equal sums, the function should return the string "balanced".
'''
def keys_v_values(dictionary):
    keys_sum = sum(dictionary.keys())
    values_sum = sum(dictionary.values())
    if (keys_sum > values_sum):
        return "keys"
    elif (keys_sum < values_sum):
        return "values"
    else:
        return "balanced"
    
#Example Usage:

dictionary1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
greater_sum = keys_v_values(dictionary1)
print(greater_sum)

dictionary2 = {100:10, 200:20, 300:30, 400:40, 500:50, 600:60}
greater_sum = keys_v_values(dictionary2)
print(greater_sum)

#Example Output:
#values
#keys