#Function

def hello():
    print("Good Morning")

hello()

#Function with argument (input inside the function is argument)

def greet(name):
    print(f"Hello {name}, Have a great day!")

greet("Vicky")

#Return

def add(a,b):
    return a+b

ans=add(10,20)
print(ans)

#*args

def add(*args):
    total=0
    for num in args:
        total+=num
    return total
print(add(1,2,3,4))

#kwargs

def profile(**kwargs):
    print("Employee details")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
profile(Emp_Name= "Vignesh",Age= 29,Gender= "Male",Designation= "Software Engineer")
