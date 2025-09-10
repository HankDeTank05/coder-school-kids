from pokemon.pokemon import Pokemon


class DragonPokemon(Pokemon):

  # constructor
  def __init__(self, name, level, hp, speed):
    #calling Pokemon"s constructor
    super().__init__(name=name,
                     type=Pokemon.DRAGON,
                     level=level,
                     hp=hp,
                     speed=speed)


class Dragonite(DragonPokemon):
  #constructor
  def __init__(self, level):
    #calling DragonPokemon's constructor
    super().__init__(name="Dragonite", level=level, hp=91, speed=80)


class Salamence(DragonPokemon):
  #constructor
  def __init__(self, level):
    #calling DragonPokemon's constructor
    super().__init__(name="Salamence", level=level, hp=95, speed=100)


class Haxorus(DragonPokemon):
  #constructor
  def __init__(self, level):
    #calling DragonPokemon's constructor
    super().__init__(name="Haxorus", level=level, hp=76, speed=97)
