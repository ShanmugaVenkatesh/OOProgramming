class A:
    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")

# Class B inherits from Class A
class B(A):
    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")

# Class C inherits from Class B
class C(B):
    def feature5(self):
        print("Feature 5 working")

c=C()

c.feature5()
c.feature4()
c.feature3()
c.feature2()
c.feature1()

# In Multilevel inheritance - Class-C inherits from Class-B and Class-B inherits form Class-A
# Hence Class C can inherit the other features that other class, which are inherited can access.
