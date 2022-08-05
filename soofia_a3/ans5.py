#5. Write a python program to as user to enter name and surname, use default argument as
# India if user does not pass surname as second para meters

fname = input("enter name")
sname = input("enter surname")

def display(fname, sname = "India"):
    if sname == "India":
        print("Name: {} \n Country: {}".format(fname,sname))
    else:
        print("Name: {} \n Surname: {}".format(fname,sname))

display(fname,sname)

print("Default argument demo")
display(fname)