from pokemon.pokemon import Pokemon


class GhostPokemon(Pokemon):

  #constructor
  def __init__(self, name, level, hp, speed):
    #calling Pokemon"s constructor
    super().__init__(name=name, type="ghost", level=level, hp=hp, speed=speed)


class Gengar(GhostPokemon):
  #constructor
  def __init__(self, level):
    #calling GhostPokemon's constructor
    super().__init__(name="Gengar", level=level, hp=60, speed=110)


class Mismagius(GhostPokemon):
  #constructor
  def __init__(self, level):
    #calling GhostPokemon's constructor
    super().__init__(name="Mismagius", level=level, hp=60, speed=105)


class Annihilape(GhostPokemon):
  #constructor
  def __init__(self, level):
    #calling GhostPokemon's constructor
    super().__init__(name="Annihilape", level=level, hp=110, speed=90)
