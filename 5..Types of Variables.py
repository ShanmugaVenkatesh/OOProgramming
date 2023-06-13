# Two types of variables:
# 1. Instance variable - as object changes, the value also changes. Variable present inside the __init__ method.
# 2. Class(static) Variable - as object changes, the value remains the same. Variable present outside the __init__ method but inside the class.

# Namespace is an area where you can create and store the object/variable.
# Instance namespace and class namespace.

class Car:
    # Class variable
    wheels=4
    def __init__(self):
        # Instance variable
        self.mil=10     
        self.company='BMW'

c1=Car()
c2=Car()

# changing the instance variable for object c1
c1.mil=15

Car.wheels=5    # changing the class variable 
print(c1.company,c1.mil,c1.wheels)
print(c2.company,c2.mil,c2.wheels)

    
 