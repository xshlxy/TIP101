'''
Problem 6:
Write a function calculate_gpa() that calculates the grade point average (GPA) for a student 
based on their course grades and returns the gpa as a float. 
The function takes in a dictionary report_card as a parameter where each key-value pair 
represents a course and the grade received in that course respectively. 
The grades are represented as strings ("A", "B", "C", "D", "F") and each grade corresponds 
to a certain number of grade points:

"A" = 4
"B" = 3
"C" = 2
"D" = 1
"F" = 0

A GPA is calculated by finding the average of all grade points.
''' 
def calculate_gpa(report_card):
    cumu_gpa=0.0
    for key in report_card:
        if report_card[key] == "A":
            cumu_gpa+=4
        elif report_card[key] == "B":
            cumu_gpa+=3
        elif report_card[key] == "C":
            cumu_gpa+=2
        elif report_card[key] == "D":
            cumu_gpa+=1
        else:
            cumu_gpa+=0
    gpa = cumu_gpa/len(report_card)
    return round(gpa,2)
#Example Usage:

report_card = {"Math": "A", "Science": "C", "History": "A", "Art": "B", "English": "B", "Spanish": "A"}
print(calculate_gpa(report_card))
#Example Output: 3.33
