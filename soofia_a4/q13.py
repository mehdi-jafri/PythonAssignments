# constructor
class A:
    def __init__(self, x) -> None:
        self.n = x
        print("Inside A's constructor, value of A's attribute \"n\" is ",self.n)

class B(A):
    def __init__(self, x, y) -> None:
        self.m = y
        super().__init__(x)
        print("Inside B's constructor, value of A's attribute \"n\" and B's attribute \"y\" is ",self.n, self.m)

class C(B):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        print("inside C's constructor and its inherited values n and m are ",self.n,self.m)

obj = C(10,20)