'''
Problem 11:
Given a dictionary tasks where keys are task names and values are priorities
 (1-10, where 10 is the highest priority), write a function 
 get_highest_priority_task() that removes the task with the highest priority 
 from the dictionary and returns its name.
If two tasks have the same priority, return the task that comes first in 
the alphabet.
'''
def get_highest_priority_task(tasks):
	item = 0
	task_name=""
	for key,value in tasks.items():
		if value > item:
			task_name=key
			item = value
		
	del tasks[task_name]
	return task_name
	
#Example Usage:

tasks = {"task1": 8, "task2": 10, "task3": 9, "task4": 10, "task5": 7}
perform_task = (get_highest_priority_task(tasks))
print(perform_task)

perform_task = (get_highest_priority_task(tasks))
print(perform_task)

perform_task = (get_highest_priority_task(tasks))
print(perform_task)

print(tasks)
#Example Output:
'''
task2
task4
task3
{"task1": 8, "task5": 7}
'''
