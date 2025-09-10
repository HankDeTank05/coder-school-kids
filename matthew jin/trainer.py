#    folder    file        data type
#    vvvvvvv vvvvvvv        vvvvvvv
from pokemon.pokemon import Pokemon

from player_input import validate_input


class Trainer:

    # constructor
    def __init__(self, party: list[Pokemon], name: str) -> None:
        self.party: list[Pokemon] = party
        self.name: str = name

    def choose(self, pokemon_index: int) -> Pokemon:
        return self.party[pokemon_index]

    def take_turn(self) -> None:
        choice = validate_input("What do you want to do?",
                                                     ["Attack", "Switch"])

    def party_usable(self) -> bool:
        number_fainted: int = 0  # the number of Pokemon fainted on a team

        for pokemon in self.party:
            # increase the "number_fainted" variable by 1 if the Pokemon in the variable called "pokemon" has fainted

            if pokemon.fainted() == True:  # if the current pokemon has fainted...
                number_fainted = number_fainted + 1  # ...increase the number of fainted Pokemon by 1

        # if not all pokemon have fainted...
        if number_fainted < len(self.party):  #
            return True  # ...the party is usable
        # otherwise, (if all pokemon have fainted...)
        else:
            return False  # ...the party is not usable
