from pokemon.pokemon import Pokemon


class RockPokemon(Pokemon)

# constructor
  def __init__(self, name, level, hp, speed):
  #calling RockPokemon"s constructor
    super().__init__(name=name,
       type="rock",
       level=level,
       hp=hp,
       speed=speed)


class Geodude(RockPokemon):
  #constructor
  def __init__(self, level):
    #calling Pokemon's constructor
    super().__init__(name="Geodude", level=level, hp=40, speed=20)

class Onix(RockPokemon):
  #constructor
  def __init__(self, level):
    #calling Pokemon's constructor
    super().__init__(name="Onix", level=level, hp=35, speed=70)

class Klawf(RockPokemon):
  #constructor
  def __init__(self, level):
    #calling Pokemon's constructor
    super().__init__(name="Klawf", level=level, hp=70, speed=75)