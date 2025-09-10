from pokemon.pokemon import Pokemon


class BugPokemon(Pokemon):

  # constructor
  def __init__(self, name, level, hp, speed):
    #calling BugPokemon"s constructor
    super().__init__(name=name, type="bug", level=level, hp=hp, speed=speed)


class Frosmoth(BugPokemon):
  #constructor
  def __init__(self, level):
    #calling Pokemon's constructor
    super().__init__(name="Frosmoth", level=level, hp=70, speed=65)


class Scatterbug(BugPokemon):
  #constructor
  def __init__(self, level):
    #calling Pokemon's constructor
    super().__init__(name="Scatterbug", level=level, hp=38, speed=35)


class Tarontula(BugPokemon):
  #constructor
  def __init__(self, level):
    #calling Pokemon's constructor
    super().__init__(name="Tarontula", level=level, hp=35, speed=20)
