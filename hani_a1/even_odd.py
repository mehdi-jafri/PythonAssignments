#predefined value
n=10

if(n%2==0):
    print("number is even".format(n))
else:print("odd".format(n))


#from user
n=int(input("enter number"))

if(n%2==0):
	print("number is even".format(n))
else:
	print("number is odd".format(n))


#function

def number():
	if(num%2==0):
		print("number is even")
	else:
		print("number is odd")

num=int(input("enter the number"))

number()