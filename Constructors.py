class Employee:
    def __init__(self,name,age,gender,designation):
        self.name = name
        self.age = age
        self.gender = gender
        self.designation = designation

    def display(self):
        print(f"Employee details: Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Designation: {self.designation}")

emp1 = Employee("Vignesh",29,"Male","Developer")
emp1.display()

