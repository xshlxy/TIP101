'''
Problem 5:
Write a function restock_inventory() that updates an inventory dictionary based on a restock list. It accepts two parameters:

current_inventory: a dictionary where each key-value pair represents an item and its current stock in the inventory
restock_list: a dictionary where each key-value pair represents an item and the quantity to be added to the inventory
If an item in restock_list is not present in the current_inventory, it should be added. The function should return the updated 
dictionary current_inventory.
'''
def restock_inventory(current_inventory, restock_list):
    for key in restock_list:
        if key in current_inventory:
            current_inventory[key]+=restock_list[key]
        else:
            current_inventory[key] = restock_list[key]
    return current_inventory

#Example Input:

current_inventory = {
    "apples": 30,
    "bananas": 15,
    "oranges": 10
}

restock_list = {
    "oranges": 20,
    "apples": 10,
    "pears": 5
}

print(restock_inventory(current_inventory,restock_list))
#Example Output:
'''
current_inventory = {
    "apples": 40,
    "bananas": 15,
    "oranges": 30,
    "pears": 5
}
'''