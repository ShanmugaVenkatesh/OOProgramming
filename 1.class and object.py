class Computer:
    def Config(self):           # self-indicates the passed argument as object
        print("i5,15GB,1TB")

comp1=Computer() # object(comp1) is created for the class(Computer)
comp2=Computer() # object(comp2) is created for the class(Computer)

#Computer.Config(comp1)
# below is the most commonly used method to call the function inside the class 
comp1.Config()  # automatically passes the comp1(object) as a object to the function
comp2.Config()