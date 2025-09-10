from pokemon.pokemon import Pokemon


class FairyPokemon(Pokemon):

# constructor
  def __init__(self, name, level, hp, speed):
  #calling FairyPokemon"s constructor
    super().__init__(name=name,
       type="fairy",
       level=level,
       hp=hp,
       speed=speed)


class Whimsicott(FairyPokemon):
  #constructor
  def __init__(self, level):
    #calling Pokemon's constructor
    super().__init__(name="Whimsicott", level=level, hp=60, speed=116)
 

class Azumarill(FairyPokemon):
  #constructor
  def __init__(self, level):
    #calling Pokemon's constructor
    super().__init__(name="Azumarill", level=level, hp=100, speed=50)

class Grimmsnarl(FairyPokemon):
  #constructor
  def __init__(self, level):
    #calling Pokemon's constructor
    super().__init__(name="Grimmsnarl", level=level, hp=95, speed=60)