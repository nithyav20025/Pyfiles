#FOR Loop

Names=["vignesh","nithya","nivyan","viniya"]

for name in Names:
    print(name.upper())

#While Loop

Password='1234'
Enter_your_password=''

while Password != Enter_your_password:
    Enter_your_password=input("Enter your correct password: ")

print("Login successful")

#Break concept

for num in range(10):
    print(num)

duplicate= [1,2,3,6,4,5,6,7,8,9]
for dup in duplicate:
    if dup == 6:
        break
    print(dup)

#Continue concept

num=[-4,-3,-2,-1,0,1,2,3,4]

for n in num:
    if n <0:
        continue
    print(n)

#While loop Ex

count=5
while count > 0:
    print(f"Countdown: {count}")
    count-=1
print("Happy New Year!")

items=[]

while True:
    item=input("Add item (Type 'done' to proceed): ")
    if item == "done":
        break
    items.append(item)
print("Items in Cart:",items)

