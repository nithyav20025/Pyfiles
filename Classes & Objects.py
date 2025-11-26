class Student:

    def say_hello(self):
        print("Hello, Good Morning")

s1= Student()
s1.say_hello()

#Multiple objects

class Intro:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def hi(self):
        print(f"Hi,I am {self.name} I live in {self.location}")

a = Intro("Vicky", "Madurai")
b = Intro("Nithya", "Villupuram")

a.hi()
b.hi()


