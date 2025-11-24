#If Condition
x=30
y=18

if x>y:
    print("x is greater than y")
else:
    print("y is less than x")

#Multiple If Condition

blood_pressure= 120

if blood_pressure >=160:
    print("BP is High")
elif blood_pressure>=130:
    print("BP is Stable")
elif blood_pressure>=90:
    print("BP is Low")
else:
    print("Under Risk")

#Nested if Condition

age=20
has_license ='no'

if age>=18:
    if  has_license=='yes':
        print("You are eligible to drive")
    else :
        print("Get a License")
else:
    print("You are not eligible to drive")