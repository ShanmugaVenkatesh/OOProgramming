class A:
    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")

# Class B inherits from Class A
class B:
    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")

# Class C inherits from Class A
class C(A,B):
    def feature5(self):
        print("Feature 5 working")

b=B()
c=C()

c.feature5()
c.feature2()
c.feature1()
c.feature3()
c.feature4()
# In Multiple inheritance - same class inherits from the diferent class
# Hence Class C can inherit the features from class A and B. 