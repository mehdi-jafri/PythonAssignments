# 12. *Write a python program to demonstrate generators
# generator example-
def myfun(n):
    i=0
    while(i<n):
        i = i+5
        yield i
    return 0

print("Calling simple generatorm function to print multiples of 5 until 30")
for x in myfun(30):
    print(x)

# fibonacci using generator
def fiboGen(n):
    a,b = 1,2

    while(a<n):
        yield a
        a,b = b, a+b

print("Calling generator function to print fibonacci series until 10")
for i in fiboGen(10):
    print(i)

