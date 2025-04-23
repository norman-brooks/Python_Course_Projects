

from abc import ABC, abstractmethod # Import abstract method


class Animal(ABC): # Parent Class
    def carnivore(self):
        print("This animal eats meat")

    @abstractmethod # Abstract method
    def jump(self):
        pass
    


class Tiger(Animal): # Child class
    def jump(self): # Abstract method from Parent class
        print("This animal can jump up to 16 feet!")

    def fur(self):
        print("The tiger has beautiful stripes in its fur.")


obj = Tiger() # Object of Child Class
obj.carnivore() # Inherited from the parent class
obj.jump() # Abstract method implemented in Tiger
obj.fur()
    
    

