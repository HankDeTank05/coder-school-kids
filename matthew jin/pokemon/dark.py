from pokemon.pokemon import Pokemon


class DarkPokemon(Pokemon):

# constructor
  def __init__(self, name, level, hp, speed):
  #calling DarkPokemon"s constructor
    super().__init__(name=name,
       type="dark",
       level=level,
       hp=hp,
       speed=speed)


class Mandibuzz(DarkPokemon):
  #constructor
  def __init__(self, level):
    #calling Pokemon's constructor
    super().__init__(name="Mandibuzz", level=level, hp=110, speed=80)

class Sharpedo(DarkPokemon):
  #constructor
  def __init__(self, level):
    #calling Pokemon's constructor
    super().__init__(name="Sharpedo", level=level, hp=70, speed=95)

class Houndoom(DarkPokemon):
  #constructor
  def __init__(self, level):
    #calling Pokemon's constructor
    super().__init__(name="Houndoom", level=level, hp=75, speed=95)