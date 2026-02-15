'''Create a class Player with:
a class variable player_count,
instance variables name and level
Track how many players were created.'''


class Player:
  player_count = 0

  def __init__(self,name,level):
    self.name = name
    self.level = level
    Player.player_count += 1

  @classmethod
  def display_count(cls):
    print(f"Total Players: {cls.player_count}")

p1= Player("Aditya","national")
p2= Player("rohit","Zoners")
p3= Player("saurav","international")

Player.display_count()