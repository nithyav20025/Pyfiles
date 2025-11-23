x = input("enter your name")
y = input("enter your age")
z = input("enter your gender")

print("Hi " + x + ", your age is: " + y + ", your gender is: " + z)

age = int(y)

if age > 30:
    print("Your age is greater than 30.")
else:
    print("Your age is 30 or less.")
