from pokemon.pokemon import Pokemon


class FightingPokemon(Pokemon)

# constructor
  def __init__(self, name, level, hp, speed):
  #calling FightingPokemon"s constructor
    super().__init__(name=name,
       type="fighting",
       level=level,
       hp=hp,
       speed=speed)


class Machamp(FightingPokemon):
  #constructor
  def __init__(self, level):
    #calling Pokemon's constructor
    super().__init__(name="Machamp", level=level, hp=90, speed=55)

class Lucario(FightingPokemon):
  #constructor
  def __init__(self, level):
    #calling Pokemon's constructor
    super().__init__(name="Lucario", level=level, hp=70, speed=90)

class Throh(FightingPokemon):
  #constructor
  def __init__(self, level):
    #calling Pokemon's constructor
    super().__init__(name="Throh", level=level, hp=120, speed=45)