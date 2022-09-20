# 7. !Write a python program to demonstrate use of multiple functions through object

class Employee:
    def __init__(self, name, id, sal) -> None:
        self.name = name
        self.id = id
        self.salary = sal

    def show(self):
        print("Name of employee", self.name)
        print("ID of the employee", self.id)
        print("Salary of the employee", self.salary)

    def salDef(self):
        if self.salary>1000:
            print("Rich")
        elif self.salary<500:
            print("poor")

emp = Employee("akram",101,5000000)

# calling function1 show() from emp object
emp.show()

# calling function2 salDef() from emp object
emp.salDef()


