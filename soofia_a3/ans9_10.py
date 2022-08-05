# write a python program to demonstrate the class

class employee:
    emp_id =101
    emp_name = "ankita"
    def display(self):
        print("employee details\n employee id:{}\n employee name: {}".format(self.emp_id,self.emp_name))


e = employee()
e.display()

# 10. write a python program to demonstrate the inheritance.
print("**********************INHERITENCE DEMO*********************")
class manager(employee):
    dept_name = "Human Resource"
    num_of_emp_under = 30
    def manager_display(self):
        print("incharge of Department: {} \n Number of employees under: {}".format(self.dept_name,self.num_of_emp_under))
    def display(self):
        return super().display()

m = manager()
m.display()
m.manager_display()