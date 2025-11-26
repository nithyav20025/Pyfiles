class Employee:
    def __init__(self,name,age,gender,designation):
        self.name = name
        self.age = age
        self.gender = gender
        self.designation = designation

    def display(self):
        print(f"Employee details: {self.name},{self.age},{self.gender},{self.designation}")

emp1 = Employee("Vignesh",29,"Male","Developer")
emp1.display()

