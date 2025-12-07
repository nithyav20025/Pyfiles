class Parent:
    def __init__(self):
        self.public_var = "Public"
        self.__private_var = "Private"     # name-mangled (private-like)
        self._protected_var = "Protected"  # protected by convention

    def access_from_same_class(self):
        print("Inside parent class:")
        print("Public:", self.public_var)
        print("Private:", self.__private_var)
        print("Protected:", self._protected_var)


class Child(Parent):

    def access_from_child_class(self):
        print("Inside child class:")
        print("Public:", self.public_var)
        # print("Private:", self.__private_var) # AttributeError if uncommented
        print("Protected:", self._protected_var)
        try:
            print("Private:", self.__private_var)
        except AttributeError:
            print("Private: ❌ Cannot access (AttributeError)")
class Stranger:
    def access_from_child_class(self, obj):
        print("Inside stranger class(Unrelated):")
        print("Public:", obj.public_var)
        print("Protected:", obj._protected_var)
        try:
            print("Private:", obj.__private_var)
        except AttributeError:
            print("Private: ❌ Cannot access (AttributeError)")



p = Parent()
p.access_from_same_class()

c = Child()
c.access_from_child_class()
