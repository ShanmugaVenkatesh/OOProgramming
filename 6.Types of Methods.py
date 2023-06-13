# Three types of methods.
# 1.Instance methods.
    # a.Accessor Methods. - used to fetch the value
    # b.Mutator Methods. -used to modify the value
# 2.Class methods.
# 3.Static methods.

class Student:
    school='Telusko'            # class variable
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    # Instance Method
    def avg(self):
        return(self.m1+self.m2+self.m3)/3
    '''
    # Accessor Method
    def get_m1(self):
        return self.m1

    # Mutator method
    def set_m1(self,value):
        return self.m1=value
    '''
    # Class Method - works with class varible
    @classmethod  #decorator to execute the class method
    def getSchool(cls):
        return cls.school
    
    # static method - uses neither class nor instance varible
    @staticmethod
    def info():
        print("This is Student class..  ")
    
s1=Student(65,46,100)
s2=Student(99,56,88)

print(s1.avg(),s2.avg())   # Instance method-because object is passed automatically

#calling the class method
print(Student.getSchool())
# calling the static method
Student.info()