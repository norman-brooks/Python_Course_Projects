# Parent Class

class Cycles:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

# The wheels have been added in as something that will change with child classes

    def wheels(self):
        pass

    def __str__(self):

        return f"{self.brand} is a cycle company that makes {self.model}s."
    
# Child Classes

class Tricycle(Cycles):
    def __init__(self, brand, material, rim_size):
        super().__init__(brand, "Radio Flyer")
        self.rim_size = rim_size
        self.material = material

# Instances for above will go at the bottom

    def __str__(self):
        return f"When I was a kid riding a {self.brand} tricyle with {self.rim_size}\" rims, and a frame made of {self.material} was the best!"
    

    def wheels(self):
        return "A tricyle has three wheels"


class Bicycle(Cycles):
    def __init__(self, brand, color, model, cost):
        super().__init__(brand, model)
        self.color = color
        self.cost = cost
        
        

    def __str__(self):
        return f"For my money riding a {self.color} {self.brand} {self.model} for under {self.cost} is worth it!"

    def wheels(self):
        return "A bicyle has two wheels."
        







# Instances
cycles = Cycles(brand = "Huffy", model = "Roadkill")
tricycle = Tricycle(brand = "Radio Flyer", material = "metal", rim_size = 7)
bicycle = Bicycle(color = "red", brand = "Schwinn", model = "Mountain Bike", cost = "1,000")

print(tricycle)
print(bicycle)
print(cycles)

print(tricycle.wheels())
print(bicycle.wheels())







