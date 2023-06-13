# If you create a object of sub class, it will try to find the init of subclass.
# If it is not found, then it will call the init of super class

class A:
    def __init__(self):
        print("init in A")

    def featur1(self):
        print("Feature 1 is working")

    def feature2(self):
        print("Feature 2 is working")

class B(A):
    def __init__(self):
        super().__init__()
        print("init in B")

    def feature3(self):
        print("Feature 3 is working")

    def feature4(self):
        print("Feature 4 is working")

# When you create object of sub class, it will call the init of sub class first.
b=B()

# super() -> to access all the features of parent class.

