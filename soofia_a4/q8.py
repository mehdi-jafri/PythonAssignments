# 8. *Write a python program to demonstrate multiple inheritance
class Parent:
    def m(self):
        print("Inside parent class")

class Child1(Parent):
    def m(self):
        print("Inside Child1 class")
        # super() is used to call parent class function
        super().m()

class Child2(Parent):
    def m(self):
        print("Inside Child2 class")

# child1 and child2 are children of parent.

class Child3(Child2, Child1):
    pass

# child3 is the child of child1 and child2
obj = Child1()
obj.m()