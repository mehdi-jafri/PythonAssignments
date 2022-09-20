# 9. !Write a python program to demonstrate overloading / polymorphism
def beverage():
    print("beverage")

def beverage(n):
    print("Cold Drink",n)
# compile time polymorpism in python can be achieved by method overloading.
#  Two methods of same name with different signatures can be defined in python.
# but to call/ exceute method overloading in python, only latest function or method that is defined will be called.
# therefore executing below line will give error 
# beverage()
# however, below line will execute successfully as it follows the latest definition of beverage() function with arguments.
beverage(56)


# in order to execute total overloaing extra if-else statement can be used along with arbitary arguments

def add(dt, *args):
    if dt == "int":
        s=0
    
    if dt == "str":
        s=" "
    
    for x in args:
        s = x +s

    print(s)

add("int",2,3,4)
add("int",2,3)
add("str","hello", "world")
    