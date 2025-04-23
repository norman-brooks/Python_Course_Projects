class Vehicle:
        def __init__(self, year, make, model):
                self.year = year
                self.make = make
                self.model = model
    # Above is our Parent Class with an argument

        def printveh(self):
            print(self.year, self.make, self.model)    

        
    # Below are children classes of "Vehicle"
class Motorcycle(Vehicle):
        def __init__(self, year, make, model, fuel):
            super().__init__(year, make, model)
            self.fuel = fuel
            

class Cycle(Vehicle):
        def __init__(self, year, make, model, pedals):
            super(). __init__ (year, make, model)
            self.pedals = pedals

    # We use the Vehicle to create and object and THEN execute the printname method


       
x = Vehicle(1971, "Harley", "Softtail")
x.printveh()
