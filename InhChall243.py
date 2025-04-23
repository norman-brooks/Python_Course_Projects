# Here we're asked to create a child class that inherits functionality from
# the parent class.

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

x = Person("Bill", "Russell")
x.printname()


class child(Person):
    pass


# Above we used the "pass" keyword. This is used when you don't want to add
# any other properties or methods to the class
