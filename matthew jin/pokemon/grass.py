'''
homework: create four empty classes
1. create a class called GrassPokemon, that derives from Pokemon (don't forget to import Pokemon)
2. create a class called Gogoat, that derives from PsychicPokemon
3. create a class called Seedot, that derives from PsychicPokemon
4. create a class called Meowscarada, that derives from PsychicPokemon
NOTE: if you need help or are confused, you can look at electric.py for reference
NOTE: remember, you're making empty classes, which look like the following:
class ClassName:
  pass
'''
from pokemon.pokemon import Pokemon


class GrassPokemon(Pokemon)

# constructor
  def __init__(self, name, level, hp, speed):
  #calling GrassPokemon"s constructor
    super().__init__(name=name,
       type="grass",
       level=level,
       hp=hp,
       speed=speed)


class Gogoat(GrassPokemon):
  #constructor
  def __init__(self, level):
    #calling Pokemon's constructor
    super().__init__(name="Gogoat", level=level, hp=123, speed=68)

class Seedot(GrassPokemon):
  #constructor
  def __init__(self, level):
    #calling Pokemon's constructor
    super().__init__(name="Seedot", level=level, hp=40, speed=30)

class Meowscrada(GrassPokemon):
  #constructor
  def __init__(self, level):
    #calling Pokemon's constructor
    super().__init__(name="Meowscrada", level=level, hp=76, speed=123)