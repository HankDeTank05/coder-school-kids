from pokemon.pokemon import Pokemon


class Party:

  # constructor
  def __init__(self):
    self.pokemon: list[Pokemon] = []

  def get_number_fainted(self) -> int:
    fainted_count = 0
    for pkmn in self.pokemon:
      # if the pokemon has fainted...
      if pkmn.fainted() == True:
        fainted_count += 1
    return fainted_count

  def get_number_of_type(self, type_name: str) -> int:
    type_count = 0
    for pkmn in self.pokemon:
      if pkmn.get_type() == type_name:
        type_count += 1
    return type_count

  def get_pokemon(self) -> Pokemon:
    pass
