#Logical operators

x=True
y=False
print(x and y)
print(x or y)
print(not y)
print(not x)

#Example 1

amount= 1200
tax=amount *0.18
total=amount+tax
print("Total amount is",total)
print("Total tax amount is",tax)

if total >= 1000:
    discount=total*0.10
    total-=discount

print("Discounted amount",total)


#Example 2

age=65
student='yes'

if age>60 or student == 'yes':
    print("yes discount")

else:
    print("no discount")
