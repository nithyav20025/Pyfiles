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

#Conditon using AND

Mark=55
Attendance=65

if Mark>=50 and Attendance<=60:
    print("You are allowed to attend the exam")
else:
    print("You are not allowed to attend the exam")

#Conditon using OR

recharge_amount=299
data_pack=1.5

if recharge_amount>=399 or data_pack>=1:
    print("eligible for free 1GB data")
else:
    print("not eligible for free data")

#Conditon using AND OR

Bill_amount=1200
offer_days="saturday"
membership_id="yes"

if (Bill_amount>=1200 and offer_days in['saturday', 'sunday']) or membership_id=='yes':
    print("20% off")
else:
    print("discount not applicable")

