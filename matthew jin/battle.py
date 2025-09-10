#     file         data type
#    vvvvvvv        vvvvvvv
import random
from trainer import Trainer
#     folder  file         data type
#    vvvvvvv vvvvvvv        vvvvvvv
from pokemon.pokemon import Pokemon
#        file              function
#    vvvvvvvvvvvv        vvvvvvvvvvvvvv
from player_input import validate_input


class Battle:

  # constructor
  def __init__(self, trainer1: Trainer, trainer2: Trainer) -> None:
    self.trainer1: Trainer = trainer1
    self.trainer2: Trainer = trainer2
    self.pokemon1: Pokemon | None = None
    
    # make the player pick a pokemon from their party
    while self.pokemon1 is None:
      try:
        # this saves the response to a variable
        user_input = input(
            "(type in a whole number) Choose which Pokemon to send out: ")
        # here we are turning user_input into a whole number, aka integer
        user_input = int(user_input)
        # check if the number is too big
        if user_input >= len(self.trainer1.party):
          print("Too big, try again")
          continue
        # check if the number is too small
        elif user_input <= -1:
          print("Too small, try again")
          continue

        # pick a pokemon from trainer1's party
        # this is trainer1's active pokemon
        self.pokemon1 = self.trainer1.choose(pokemon_index=user_input)
      except (EOFError, KeyboardInterrupt):
        # If there's no interactive input available, default to first pokemon
        print("No interactive input available, defaulting to first Pokemon")
        self.pokemon1 = self.trainer1.choose(pokemon_index=0)
      except ValueError:
        print("Please enter a valid number")
      #Here we are taking a pokemon from trainer.2
      #this is trainer2's active pokemon
      self.pokemon2: Pokemon = self.trainer2.choose(pokemon_index=0)

  def start(self) -> None:
    while self.trainer1.party_usable() and self.trainer2.party_usable():
      self.take_turn()
    # by this point in the code, the battle is over
  
  def take_turn(self) -> None:
    ATTACK = 0
    SWITCH = 1
    prompt: str = "What do you want to do?"
    options: list[str] = ["Attack", "Switch"]
    if self.pokemon1.speed > self.pokemon2.speed:
      # trainer 1 takes their turn
      # HOMEWORK (part 1)
      # make a variable called choice, and assign the result of validate_input to it
      choice = validate_input(prompt, options)
      if choice == ATTACK:
        print()
        # TODO call attack function here: self.pokemon.attack()
      
    else:
      # trainer 2 takes their turn
      # HOMEWORK (part 2)
      # make a variable called choice, and assign a random number to it.
      # the random number must be in the range of valid indices (indexes) for the options list, created above
      choice = random.randint(0, len(options)-1)
