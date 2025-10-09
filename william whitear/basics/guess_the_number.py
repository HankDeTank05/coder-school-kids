import random

min: int = 0
max: int = 150

number: int = random.randint(min, max)

prompt: str = f"guess a number between {min} and {max}"

print(prompt)

# making guess an incorrect answer because if it is equal to number the game ends
guess: int = min - 1

while guess != number:
    response: str = input("what is your guess ")

    if response.isnumeric():
        guess = int(response) #

        if guess < number:
            print("too low")
        elif guess > number:
            print("too high")

# if you got to this point in code you got it!
print('you got it!')