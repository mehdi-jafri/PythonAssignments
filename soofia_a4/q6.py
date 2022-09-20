# Defining child class class 
class Parent(): 
    def __init__ ( self ): 
         self .value = "car" 
    def show ( self ): 
         print ( self .value)

class child(Parent):
    def __init__ ( self ):
        self .value = "BMW,Alfaromeo,Bently" 
    def show ( self ): 
        print ( self .value) 
        
p1 = Parent() 
c1 = child() 
p1.show() 
c1.show()