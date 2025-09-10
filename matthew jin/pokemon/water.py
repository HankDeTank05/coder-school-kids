from pokemon.pokemon import Pokemon


class WaterPokemon(Pokemon)

# constructor
  def __init__(self, name, level, hp, speed):
  #calling WaterPokemon"s constructor
    super().__init__(name=name,
       type="water",
       level=level,
       hp=hp,
       speed=speed)


class Psyduck(WaterPokemon):
  #constructor
  def __init__(self, level):
    #calling Pokemon's constructor
    super().__init__(name="Psyduck", level=level, hp=50, speed=55)

class Quaquaval(WaterPokemon):
  #constructor
  def __init__(self, level):
    #calling Pokemon's constructor
    super().__init__(name="Quaquaval", level=level, hp=85, speed=85)

class Greninja(WaterPokemon):
  #constructor
  def __init__(self, level):
    #calling Pokemon's constructor
    super().__init__(name="Quaquaval", level=level, hp=72, speed=122)