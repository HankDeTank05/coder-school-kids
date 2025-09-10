from pokemon.pokemon import Pokemon


class FirePokemon(Pokemon):

  #constructor
  def __init__(self, name, level, hp, speed):
    #calling Pokemon"s constructor
    super().__init__(name=name, type="fire", level=level, hp=hp, speed=speed)


class Charizard(FirePokemon):
  #constructor
  def __init__(self, level):
    #calling FirePokemon's constructor
    super().__init__(name="Charizard", level=level, hp=78, speed=100)


class Scovillan(FirePokemon):
  #constructor
  def __init__(self, level):
    #calling FirePokemon's constructor
    super().__init__(name="Scovillan", level=level, hp=65, speed=75)


class Camerupt(FirePokemon):
  #constructor
  def __init__(self, level):
    #calling FirePokemon's constructor
    super().__init__(name="Camerupt", level=level, hp=70, speed=40)
