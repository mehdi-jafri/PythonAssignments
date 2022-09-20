
class Person:
    def __init__(self,name,id) -> None:
        self.name = name
        self.id = id

    def show(self):
        print("name is {} and id is {}".format(self.name, self.id))

class Employee(Person):
    def __init__(self,name,id,sal) -> None:
        # instead of defining name id again in Employee we simply call the parent class constructor through super()
        super().__init__(name,id)
        self.salary = sal
        
    def show(self):
        super().show()
        # instead of printing name,id again in Employee we simply call the parent class show() through super()
        print("salary is {}".format(self.salary))

obj = Employee("Ankita",101,50000)
obj.show()