#by user
a=int(input("enter the radius of a circle"))

pi=3.14

m=pi*a*a

print(m)

#using math module
#import math module
from math import pi
r=int(input("enter radius"))
area= pi*r**2

print(area)


#using function
def radius():
	a=2
	print(pi*a**2)
radius()