'''
homework: create four empty classes
1. create a class called NormalPokemon, that derives from Pokemon (don't forget to import Pokemon)
2. create a class called Meowth, that derives from PsychicPokemon
3. create a class called Maushold, that derives from PsychicPokemon
4. create a class called Braviary, that derives from PsychicPokemon
NOTE: if you need help or are confused, you can look at electric.py for reference
NOTE: remember, you're making empty classes, which look like the following:
class ClassName:
  pass
'''
from pokemon.pokemon import Pokemon


class NormalPokemon(Pokemon):
 
  # constructor
  def __init__(self, name, level, hp, speed):
    #calling Pokemon"s constructor
    super().__init__(name=name, type="normal", level=level, hp=hp, speed=speed)


class Meowth(NormalPokemon):
  #constructor
  def __init__(self, level):
    #calling NormalPokemon's constructor
    super().__init__(name="Meowth", level=level, hp=40, speed=90)

class Maushold(NormalPokemon):
  #constructor
  def __init__(self, level):
    #calling NormalPokemon's constructor
    super().__init__(name="Maushold", level=level, hp=74, speed=111)

class Braviary(NormalPokemon):
  #constructor
  def __init__(self, level):
    #calling NormalPokemon's constructor
    super().__init__(name="Braviary", level=level, hp=100, speed=80)