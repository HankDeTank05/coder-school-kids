import random

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
correct = "*"
wrong_position = "/"
incorrect = "!"
not_played = "-"

letters_played = {}

for letter in letters:
  # print(letter)
  letters_played[letter] = not_played
  #print(f"{letter} : {letters_played[letter]}")

potential_words = [
  "APPLE",
  "BREAD",
  "CHAIR",
  "DANCE",
  "FLAME",
  "GRASS",
  "LIGHT",
  "MUSIC",
  "NIGHT",
  "PAINT",
  "QUIET",
  "RIVER",
  "STORM",
  "TABLE",
  "WORLD",
  "CROWN",
  "SWEET",
  "BLAZE",
  "CRISP",
  "FROST",
  "GHOST",
  "HONEY",
  "IVORY",
  "LEMON",
  "MAPLE",
  "PEACH",
  "QUEEN",
  "ROCKY",
  "SHORE",
  "TWIST"
]

for word in potential_words:
  assert(len(word) == 5) # crash the program if length of word isnt 5 letters
  assert(word.isalpha() == True) # crash the program if the word isnt all letters
  word = word.upper() # make the word uppercase

correct_word = random.choice(potential_words)
guessed_word = None

def print_red(string, end):
  print(f"\033[91m{string}\033[00m", end=end)
  
def print_green(string, end):
  print(f"\033[92m{string}\033[00m", end=end)
  
def print_yellow(string, end):
  print(f"\033[93m{string}\033[00m", end=end)

def play():
  global guessed_word
  while guessed_word != correct_word:
    # makes sure guessed word is 5 letters
    guess_is_valid = False
    while not guess_is_valid:
      guessed_word = input("guess: ")
      #print(guessed_word)
      if len(guessed_word) != 5:
        print("must type five letters, try again")
        guess_is_valid = False
      elif not guessed_word.isalpha():
        print("type letters only, try again")
        guess_is_valid = False
      else:
        guess_is_valid = True

    # evaluate guessed word
    for i in range(len(guessed_word)):
      guessed_letter = guessed_word[i]
      correct_letter = correct_word[i]
      # check if it's exactly correct
      if correct_letter == guessed_letter:
        letters_played[guessed_letter] = correct
      # if not, check if it's in the wrong position
      elif guessed_letter in correct_word:
        letters_played[guessed_letter] = wrong_position
      # if not, it's incorrect
      else:
        letters_played[guessed_letter] = incorrect

    # display guessed letters
    # print(letters)
    for letter in letters:
      symbol = letters_played[letter]
      if symbol == correct:
        print_green(letter, end="")
        
      elif symbol == wrong_position:
        print_yellow(letter, end="")
        
      elif symbol == incorrect:
        print_red(letter, end="")

      else:
        print(letter, end="")
    print("\n")
  print("You win")

play()
