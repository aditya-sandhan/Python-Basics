from abc import ABC, abstractmethod

class Animal(ABC):      #Abstract class
    @abstractmethod     #Abstarct Method 
    def make_sound(self):
        pass

class Lion(Animal):
    def make_sound(self):
        print("Roar!")

class Cow(Animal):
    def make_sound(self):
        print("Moo!")

l = Lion()
l.make_sound()

c = Cow()
c.make_sound()