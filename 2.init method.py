class Computer:
    def __init__(self,cpu,ram):     # self-indicates the passed argument as object
        self.cpu=cpu                # cpu, ram are arguments. To assign it to a object, (object is passed automatically, and stored as a self-keyword)
        self.ram=ram                # Hence, assigning it to a object by using self(object) to store it in a variable.

    def Config(self):
        print("Config is ", self.cpu,self.ram)      # cpu, ram are not local variables, it belongs to object. So using self(object) to access it.

# passing arguments in the creation of the object.
comp1=Computer('i6',16)
comp2=Computer('Raizen',8)

# __init__  is a constructor. When object is created, it is called automatically.

comp1.Config()
comp2.Config()