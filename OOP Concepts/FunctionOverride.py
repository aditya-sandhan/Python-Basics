class Animal:       #general class
    def sound(self):
        print("Animals make sound!")

class dog(Animal):  #specific class
    def sound(self):
        print("Bark!")

class cat(Animal):  #specific class
    def sound(self):
        print("Meoww!")

d = dog()  #Dog class overrode sound of Animal class 
c = cat()  #Cat class overrode sound of Animal class 

for x in [d,c]:
    x.sound()