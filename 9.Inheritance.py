# Class A - Parent class/Super class
# Class B - child class/sub class

class A:
    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")

class B(A):                         # Class B - inherit the features from class A
    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")

# creating the class for class-A
a=A()
a.feature1()

b=B()
# methods from the Class A (parent class) can also be inherited/accesible through child class (class B)
b.feature1()
b.feature2()
b.feature3()
b.feature4()

# Single Inheritance - Class B inherits the features form Class A.
