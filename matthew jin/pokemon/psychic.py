'''
homework: create four empty classes
1. create a class called PsychicPokemon, that derives from Pokemon (don't forget to import Pokemon)
2. create a class called Alakazam, that derives from PsychicPokemon
3. create a class called Metagross, that derives from PsychicPokemon
4. create a class called Wobbuffet, that derives from PsychicPokemon
NOTE: if you need help or are confused, you can look at electric.py for reference
NOTE: remember, you're making empty classes, which look like the following:
class ClassName:
  pass
'''
from pokemon.pokemon import Pokemon


class PsychicPokemon(Pokemon)

# constructor
  def __init__(self, name, level, hp, speed):
  #calling PsychicPokemon"s constructor
    super().__init__(name=name,
       type="psychic",
       level=level,
       hp=hp,
       speed=speed)


class Alakazam(PsychicPokemon):
  #constructor
  def __init__(self, level):
    #calling Pokemon's constructor
    super().__init__(name="Alakazam", level=level, hp=55, speed=120)


class Metagross(PsychicPokemon):
  #constructor
  def __init__(self, level):
    #calling Pokemon's constructor
    super().__init__(name="Metagross", level=level, hp=80, speed=70)


class Wobbuffet(PsychicPokemon):
  #constructor
  def __init__(self, level):
    #calling Pokemon's constructor
    super().__init__(name="Wobbuffet", level=level, hp=190, speed=33)