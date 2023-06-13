class Person:
    def __init__(self):
        self.name='Ravi'
        self.age=30

    def update(self):
        self.age=25
    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False

c1=Person()
c2=Person()

# Changing the variable name:
c2.name='Sam'

c1.update() 

# When 2 or more objects present for a class, the self - object pointer points/refers to the current object.
# To refer a one object , when there is more than 2 object --> self is used.
# c1.update() -> automatically c1 object is passed and assigned to self in method. So, c1.age will be updated.
print(c1.name)
print(c2.name)
print(c1.age)
print(c2.age)

if c1.compare(c2):          # c1(object) assigned to self automatically and c2 is passed as an argument (other)
    print("Ages are same")
else:
    print("Ages are different")
