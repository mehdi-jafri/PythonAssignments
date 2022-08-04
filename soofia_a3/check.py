# Write a python program to create a module named “check” which contains various
# functions to check even and odd numbers, print specified series, add item in the list etc.

def even_odd(*a):
    ev =[]
    od =[]
    i=0
    while(i<len(a)):
        if a[i]%2 == 0:
            ev.append(a[i])
        else:
            od.append(a[i])
        i += 1
    print("even numbers are: ",ev)
    print("odd numbers are: ",od)

# even_odd(2,3,4,5,6,7)

def check_even_odd(a):
    if a%2 == 0:
        print("{} is an even number".format(a))
    else:
        print("{} is an odd number".format(a))

# check_even_odd(4)

def series(n):
    for i in range(1,n+1):
        print(i)

# series(5)

def add_list(list):
    n = int(input("how many fruits you want to insert : "))
    i = 0
    while(i<n):
        temp = input("enter fruit to insert in list")
        list.append(temp)
        i = i+1
    
    print("Youtr list is : ",list)

# add_list()

