from pokemon.pokemon import Pokemon


class GroundPokemon(Pokemon):

  # constructor
  def __init__(self, name, level, hp, speed):
  #calling Pokemon"s constructor
    super().__init__(name=name,
       type="grass",
       level=level,
       hp=hp,
       speed=speed)


class Hippowadon(GroundPokemon):

  #constructor
  def __init__(self, level):
    #calling GroundPokemon constructor
    super().__init__(name="Hippowadon", level=level, hp=108, speed=47)

class Sandaconda(GroundPokemon):

  #constructor
  def __init__(self, level):
    #calling GroundPokemon constructor
    super().__init__(name="Sandaconda", level=level, hp=72, speed=71)

class Krookodile(GroundPokemon):

  #constructor
  def __init__(self, level):
    #calling GroundPokemon constructor
    super().__init__(name="Krookodile", level=level, hp=95, speed=92)