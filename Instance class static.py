class Student:
    Specialisation = "Accountancy"

    @classmethod
    def change_specialisation(cls, new_specialisation):
        cls.Specialisation = new_specialisation

    @staticmethod
    def try_change_specialisation(new_specialisation):
        Student.Specialisation = new_specialisation

Student.change_specialisation("Commerce")
print("After class method:", Student.Specialisation)

Student.try_change_specialisation("Economics")
print("After static method:", Student.Specialisation)
