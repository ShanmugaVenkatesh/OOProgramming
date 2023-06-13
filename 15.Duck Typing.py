class Pycharm:
    def execute(self):
        print("Compiling")
        print("Running")

class Editor:
    def execute(self):
        print("spell check")
        print("compiling")
        print("running")

class Laptop:
    def code(self,ide):
        ide.execute()

lap=Laptop()
edit=Pycharm()
# edit=Editor()


# calling the code-method in Laptop class, by passing object(edit) to invoke the execute() method. edit object is passed, because of execute method present in the Pycharm class.
lap.code(edit)

'''
Another class(Editor) is created and object for that is edit - which is commented above. If it is uncommented and 'edit=Pycharm()' is commented , then execute method of the Editor will be executed.
'''