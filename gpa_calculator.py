"""
Mallory Rich
IS 303

Inputs:
- student name
- grade for 3 classes
- credits for 3 classes

Processes:
- calculate GPA using the grades and credit total

Outputs:
- GPA
- report card for student

"""

# INPUTS
name = input("Student Name: ")
grade1 = int(input("Course 1 grade point: "))
grade2 = int(input("Course 2 grade point: "))
grade3 = int(input("Course 3 grade point: "))
credit1 = int(input("Course 1 credits: "))
credit2 = int(input("Course 2 credits: "))
credit3 = int(input("Course 3 credits: "))

# PROCESSES
total_credits = credit1 + credit2 + credit3
gpa = (grade1 * credit1 + grade2 * credit2 + grade3 * credit3) / total_credits

# OUTPUTS
print (f"{name}'s Report Card")
print (f"Credits Taken: {total_credits}")
print (f"Course 1: {grade1} Credits: {credit1}\n"
       f"Course 2: {grade2} Credits: {credit2}\n"
       f"Course 3: {grade3} Credits: {credit3}")
print (f"GPA: {gpa:.2f}")