'''
How does a prompt work?
1. Display prompt text
2. Process response
'''

LETTERS: str = "abcdefghijklmnopqrstuvwxyz"

def prompt(prompt_text: str, options: list[str]) -> None:
    #Displays prompt text
    print(prompt_text)
    #Displays the options
    for index in range(len(options)):
        # print(index)
        letter: str = LETTERS[index]
        option: str = options[index]
        print(f"\t{letter}. {option}")
    response: str = input("Type a letter: ")
    response = response.lower() #Makes the letters in the response in lower case
    if len(response) > 1:
        print("Response is too long!")
    elif response not in LETTERS:
        print("Response is not a letter!")

    #Process response

if __name__ == "__main__":
    # put prompt testing code in this if block
    prompt("Where would you like to start?", ["Pitcher, OK", "Barrington, IL"])
else:
    pass