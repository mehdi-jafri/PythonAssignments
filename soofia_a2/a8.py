a=int(input("enter no a= "))
b=int(input("enter 2nd no b= "))
# c=a
# a=b
# b=c
# print("after swapping the no are : a= ",a," b = ",b)

print("Before swapping a = {} b ={}".format(a,b))
a,b = b,a
print("After Swapping a = {} b ={}".format(a,b))