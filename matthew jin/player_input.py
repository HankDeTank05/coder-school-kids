def validate_input(prompt: str, options: list[str]) -> int:
  # display the prompt
  print(prompt)

  # display (and number) the options for the player
  for i in range(len(options)):
    print(i, end=". ")
    print(options[i])

  #
  while True:
    user_input: str = input("type a number, then press enter: ")
    # kinds of invald input

    # an empty string
    if len(user_input) == 0:
      print("Try again, you didn't type anything, next time type something")

    # a string with no numbers, or a string that has more than just numbers
    # a number with a "." in it
    elif not user_input.isnumeric():
      print(
          "Try again, you either didn't have a number or you had more than just a number, next time try only using numbers (no punctuation allowed)"
      )

    # a number that is too big
    elif int(user_input) >= len(options):
      print(
          "Try again, your number was too big, next time write a smaller number"
      )

    else:
      index: int = int(user_input)
      break

  print(f"You chose option number {index}: \"{options[index]}\"")

  return index
