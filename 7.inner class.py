# Inner class is used to avoid creating new another class for the class, which has the same properties or link between them.
# object of inner class can be created outside the outer class or outside the inner class but inside the outer class. 

class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

        # Creting the object of inner class --> outside the inner class but inside the outer class
        self.Lap=self.Laptop()  # self.Laptop() --> Taking the object(outer class) to the inner class

    def display(self):
        print(self.name,self.rollno)

    # Inner class
    class Laptop:
        def __init__(self):
            self.brand='HP'
            self.cpu='i5'
            self.ram='8GP'

        def show(self):
            print(self.brand,self.cpu,self.ram)

s1=Student('Navin',1)

# calling the display method to print the details of the student
s1.display()

# calling the show method present inside the inner class
s1.Lap.show()

# Instead of using below print statement to print the details, we can use show method to display.
# print(s1.name,s1.rollno)