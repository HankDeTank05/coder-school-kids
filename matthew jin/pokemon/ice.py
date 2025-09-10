from pokemon.pokemon import Pokemon


class IcePokemon(Pokemon)

# constructor
  def __init__(self, name, level, hp, speed):
  #calling IcePokemon"s constructor
    super().__init__(name=name,
       type="ice",
       level=level,
       hp=hp,
       speed=speed)


class Weavile(IcePokemon):
  #constructor
  def __init__(self, level):
    #calling Pokemon's constructor
    super().__init__(name="Weavile", level=level, hp=70, speed=125)

class Delibird(IcePokemon):
  #constructor
  def __init__(self, level):
    #calling Pokemon's constructor
    super().__init__(name="Delibird", level=level, hp=45, speed=75)

class Cetoddle(IcePokemon):
  #constructor
  def __init__(self, level):
    #calling Pokemon's constructor
    super().__init__(name="Cetoddle", level=level, hp=108, speed=43)