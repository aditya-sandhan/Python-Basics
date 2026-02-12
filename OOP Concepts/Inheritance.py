class Animal:
    Location = "South africa"

class lion(Animal):
    def __init__(self,sound,food):
        self.sound = sound
        self.food = food

class wolf(Animal):
    def __init__(self, Number):
        self.Number = Number

l1 = lion("ROAR","Flesh")
print(l1.food, l1.sound, l1.Location)

w1 = wolf(20)
print(f"There are total {w1.Number} of Wolf's in {w1.Location}")