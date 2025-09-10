class Move:
  def __init__(self, name: str, damage: int, accuracy: int, type):
    assert(len(name) > 0) # if the move name is less than or equal to 0, crash the program 
    self.name: str = name
    assert(damage >= 0) # if damage is less than 0, crash the program
    self.damage: int = damage
    assert(0 <= accuracy <= 100) # if the accuracy is not in the range 0-100, then crash the program
    self.accuracy: int = accuracy
    self.type = type