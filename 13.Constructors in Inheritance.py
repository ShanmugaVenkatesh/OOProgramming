# In Multiple Inheritance, here class-C inherits fromm class A and B
# creating object for Class-C, then it checks for init method in class-C and executes.
# If init is absent in class-C, then checks for the init in parent class.
# It uses MRO (Method Resolution Order) --> when super() class is used to access the features of the parent class in multiple inheritance, it takes from 1st parent class(A) and then to next (class-B)  [Left to right]

class A:
    def __init__(self):
        print("init in A")

    def featur1(self):
        print("Feature 1-A is working")

    def feature2(self):
        print("Feature 2 is working")

class B:
    def __init__(self):
        super().__init__()
        print("init in B")

    def feature1(self):
        print("Feature 1 -B is working")

    def feature4(self):
        print("Feature 4 is working")

class C(A,B):
    def __init__(self):
        print("init in C")
        super().__init__()

    def feat(self):
        # using super() class to access the method of parent class
        super().feature2()

# creating object for class C
c=C()

# it uses Method Resolution Order [left to right], 1st parent (class-A) feature1 is accessed.
c.featur1()

c.feat()