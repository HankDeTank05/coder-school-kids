from pokemon.pokemon import Pokemon


class PoisonPokemon(Pokemon):

  # constructor
  def __init__(self, name, level, hp, speed):
  #calling Pokemon"s constructor
    super().__init__(name=name,
       type="poison",
       level=level,
       hp=hp,
       speed=speed)


class Arbok(PoisonPokemon):
  #constructor
  def __init(self, level):
    #calling PoisonPokemon's constructor
    super().__init__(name="Arbok", level=level, hp=60, speed=80)

class Weezing(PoisonPokemon):
  #constructor
  def __init(self, level):
    #calling PoisonPokemon's constructor
    super().__init__(name="Weezing", level=level, hp=65, speed=60)

class Drapion(PoisonPokemon):
  #constructor
  def __init(self, level):
    #calling PoisonPokemon's constructor
    super().__init__(name="Drapion", level=level, hp=70, speed=95)