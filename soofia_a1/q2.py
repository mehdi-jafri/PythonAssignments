#write a program to calculate interest and display it

p = float(input("enter principl amount"))
r = float(input("enter rate of interest"))
t = float(input("enter time"))

interest = ((p*r*t)/100)

# print("simple interest is: {}".format(interest))
print("simple interest is: ",interest)