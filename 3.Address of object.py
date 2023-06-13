class Computer:
    pass

c1=Computer()
c2=Computer()

#printing the address of the object.
print(id(c1))
print(id(c2))

# object occupy some space in the heap memory and gets stored there.
# Each time of execution, new objects are created. Hence address of the object varies.
# Size of the object depends on the size of each variable present.
# Constructor allocates the size of the object.