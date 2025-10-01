import random

min: int = 0
max: int = 150

number: int = random.randint(min, max)

prompt: str = f"guess a number between {min} and {max}"

print(prompt)

guess: int = min - 1

while guess != number:
    response: str = input("what is your guess ")

    if response.isnumeric():
        guess = int(response)
        if guess < number:
            print("too low")
        elif guess > number:
            print("too high")

print('you got it!')