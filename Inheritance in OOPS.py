class dad:

    def home(self):
        print("Hello, I am your Father")


class son(dad):

    def factory(self):
        print("Hello, Father")

s=son()
s.home()
s.factory()


class app1:

    def v1(self):
        print("Click to order")

class app1_1(app1):

    def v2(self):
        print("Online payment")

a=app1_1()
a.v1()
a.v2()