# destructor
class A:
    def __init__(self, x) -> None:
        self.n = x
        print("Inside A's constructor, value of A's attribute \"n\" is ",self.n)

    def __del__(self):
        print("Destructor called, A deleted.")

class B(A):
    def __init__(self, x, y) -> None:
        self.m = y
        super().__init__(x)
        print("Inside B's constructor, value of A's attribute \"n\" and B's attribute \"y\" is ",self.n, self.m)

    def __del__(self):
        super().__del__()
        print("Destructor called, B deleted.")

obj = B(10,20)