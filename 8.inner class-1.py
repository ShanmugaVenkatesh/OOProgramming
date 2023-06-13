# Another method to create object for inner class.

class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

    def display(self):
        print(self.name,self.rollno)

    class Laptop:
        def __init__(self):
            self.brand="HP"
            self.cpu="i5"
            self.ram="8GP"
        def show(self):
            print(self.brand,self.cpu,self.ram)

# creating the object for outer class
s1=Student('Harsh',2)

# calling the display in outer class
s1.display()

# creating the object for inner class, (outside the outer class)
lap1=s1.Laptop()

lap1.show()


