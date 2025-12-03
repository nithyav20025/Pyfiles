from abc import ABC, abstractmethod

class Feature_update(ABC):
    @abstractmethod
    def Login(self):
        pass

    @abstractmethod
    def Logout(self):
        pass

    @abstractmethod
    def Password(self):
        pass

    @abstractmethod
    def correctpassword(self):
        pass

class UserFeature(Feature_update):
    def Login(self):
        print("User logged in")

    def Logout(self):
        print("User logged out")

    def Password(self):
        print("Enter Password")

    def correctpassword(self):
        print("Password is correct")

# Usage
user = UserFeature()
user.Login()
user.correctpassword()
user.Password()
user.Logout()
