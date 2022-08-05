# 3. *Write a python program to do the following on python dictionary

Employee = { 'Id' : 1001 , 'name' : 'Sachin' , 'Dept' : 'IT' , 'age' : 26 } 

# a. Add one key value pair
Employee.update({"Salary":100000})
print(Employee)

# b. Update Employee name
Employee["name"] = "Virat"
print(Employee)

# c. Remove age
del Employee['age']
print(Employee)
