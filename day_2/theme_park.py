'''
INPUTS
- age
- day of week
- height
- VIP
- signed waiver
- parent present

PROCESSES
- use variables to identify which rides are available

OUTPUTS
- a list of rides 
'''

#INPUTs
age = int(input("Age: "))
day_of_week = input("Day of Week: ").lower()
height = int(input("Height in inches: "))
vip = input("VIP? yes/no ").lower()
signed_waiver = input("Signed waiver? yes/no ").lower()
parent_present = input("Parent present? yes/no ").lower()

#PROCESSES
#Megadrop
if age >= 14 and signed_waiver == "yes":
    if height >= 54:
        print("Megadrop")
    elif height >= 50 and vip == "yes":
        print ("Megadrop")

#Thunderbolt
if age >= 10 and height >= 48 and day_of_week != "monday":
    print("Thunderbolt")

#Kiddie Coaster
if age >= 8 or parent_present == "yes":
    print("Kiddie Coaster")
else:
    print("No ride found")