"""
INPUTS
- height
- weight
- name

PROCESSES
- input validations
- calculate BMI = weight / height^2 * 703
- categorize BMI
    underweight <18.5
    healthy 18.5-24.9
    overweight 30.0-39.9
    severe obesity 40.0+

OUTPUT
-  Report for an individual (name, bmi)
"""

#Inputs
name = input("Name: ")
height = input("Height in inches: ")
weight = input("Weight in pounds: ")

#Input Validation
ready_to_process = True

height = height.replace(".","",1)
height_is_int = height.isdigit()
if height_is_int == True:
    height = int(height)
height_is_reasonable = False
if height_is_int and height < 140 and height > 12:
    height_is_reasonable = True

if height_is_int == False or height_is_reasonable == False:
    print ("You entered an unexpected height. Please use whole numbers between 1 and 140.")
    ready_to_process = False

weight = weight.replace(".","",1)
weight_is_int = weight.isdigit()
if weight_is_int == True:
    weight = int(weight)
weight_is_reasonable = False
if weight_is_int and weight < 1200 and weight > 4:
    weight_is_reasonable = True

if weight_is_int == False or weight_is_reasonable == False:
    print ("You entered an unexpected weight. Please use whole numbers between 13 and 1200.")
    ready_to_process = False

#PROCESS
if ready_to_process == True:
    bmi = (weight / height**2) * 703
    bmi_category = ""
    if bmi < 18.5:
        bmi_category = "underweight"
    elif bmi <=24.9:
        bmi_category = "healthy"
    elif bmi <=29.9:
        bmi_category = "overweight"
    elif bmi <=39.9:
        bmi_category = "obesity"
    else:
        bmi_category = "severe obesity"

#OUPUT
print(f"\n"
    f"Report for {name}\n"
    f"Your BMI is {int(bmi)}\n"
    f"Your BMI category is: {bmi_category}\n")