class Pokemon:

  BUG = "bug"
  DARK = "dark"
  DRAGON = "dragon"
  ELECTRIC = "electric"
  FAIRY = "fairy"
  FIGHTING = "fighting"
  FIRE = "fire"
  GHOST = "ghost"
  FLYING = "flying"
  GRASS = "grass"
  GROUND = "ground"
  ICE = "ice"
  NORMAL = "normal"
  POISON = "poison"
  PSYCHIC = "psychic"
  ROCK = "rock"
  STEEL = "steel"
  WATER = "water"

  # constructor
  def __init__(self, name: str, type: str, level: int, hp: int, speed: int):
    self.name = name
    self.type: str = type
    self.level = level
    self.max_hp = hp
    self.curr_hp = self.max_hp
    self.speed = speed
    self.moves = []

  def fainted(self) -> bool:
    if self.curr_hp <= 0:
      return True
    else:
      return False

  def attack(self, move_number, target_pokemon):

    damage = self.moves[move_number].damage

    # Line (number) takes pokemon_HP and the move's damage and subtracts the damage from the HP
    target_pokemon.HP = target_pokemon.HP - damage
    print(self.name + " did " + str(damage) + " to " + target_pokemon.name)

  def learn(self, move):
    self.moves.append(move)

  def get_type(self) -> str:
    return self.type
