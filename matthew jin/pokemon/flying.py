from pokemon.pokemon import Pokemon


class FlyingPokemon(Pokemon):

  #constructor
  def __init__(self, name, level, hp, speed):
    #calling Pokemon"s constructor
    super().__init__(name=name,
       type="flying",
       level=level,
       hp=hp,
       speed=speed)


class Pidgeot(FlyingPokemon):
  #constructor
  def __init__(self, level):
    #calling FlyingPokemon's constructor
    super().__init__(name="Pidgeot", level=level, hp=83, speed=101)

class Staraptor(FlyingPokemon):
  #constructor
  def __init__(self, level):
    #calling FlyingPokemon's constructor
    super().__init__(name="Staraptor", level=level, hp=85, speed=100)

class Noctowl(FlyingPokemon):
  #constructor
  def __init__(self, level):
    #calling FlyingPokemon's constructor
    super().__init__(name="Noctowl", level=level, hp=100, speed=70)