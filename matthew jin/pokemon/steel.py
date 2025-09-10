from pokemon.pokemon import Pokemon


class SteelPokemon(Pokemon)

# constructor
  def __init__(self, name, level, hp, speed):
  #calling SteelPokemon"s constructor
    super().__init__(name=name,
       type="steel",
       level=level,
       hp=hp,
       speed=speed)


class Aegislash(SteelPokemon):
  #constructor
  def __init__(self, level):
    #calling Pokemon's constructor
    super().__init__(name="Aegislash", level=level, hp=60, speed=60)

class Ferrothorn(SteelPokemon):
  #constructor
  def __init__(self, level):
    #calling Pokemon's constructor
    super().__init__(name="Ferrothorn", level=level, hp=74, speed=20)
  pass

class Copperajah(SteelPokemon):
  #constructor
  def __init__(self, level):
    #calling Pokemon's constructor
    super().__init__(name="Copperajah", level=level, hp=122, speed=30)