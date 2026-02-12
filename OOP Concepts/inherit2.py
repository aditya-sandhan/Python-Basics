class Animal:
    def __init__(self,name):
        self.name = name

class dog(Animal):
    def __init__(self,sound,name):
        # Animal.__init__(self,name)  
        super().__init__(name)
        self.sound = sound 

d1 = dog("bark","labruodog")
print(d1.name)
