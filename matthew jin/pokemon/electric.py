from pokemon.pokemon import Pokemon


class ElectricPokemon(Pokemon):

  # constructor
  def __init__(self, name, level, hp, speed):
    # calling Pokemon's constructor
    super().__init__(name=name,
                     type="electric",
                     level=level,
                     hp=hp,
                     speed=speed)


class Raichu(ElectricPokemon):

  # constructor
  def __init__(self, level):
    #calling ElectricPokemon's constructor
    super().__init__(name="Raichu", level=level, hp=60, speed=110)


class RotomWash(ElectricPokemon):
  
  #constructor
  def __init__(self, level):
    #calling ElectricPokemon's constructor
    super().__init__(name="Rotom-Wash", level=level, hp=50, speed=86)


class Magnemite(ElectricPokemon):
  #constructor
  def __init__(self, level):
    #calling ElectricPokemon's constructor
    super().__init__(name="Magnemite", level=level, hp=25, speed=45)

