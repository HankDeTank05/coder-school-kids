'''
How does a prompt work?
1. Display prompt text
2. Process response
'''

LETTERS: str = "abcdefghijklmnopqrstuvwxyz"

'''
Data to give
Start by giving a prompt which should ask the player a question
Next, you should give the player options to choose from

What this function does
1. It prints the given prompt 
2. Prints options from the given list, one option per line*
3. It then prompts the user to type the letter coresponding to the option that they choose, and waits for their response
4. It checks to see if the typed input is accceptable 
5. Converts from the typed letter to the option that corresponds to that letter 

what it will give back
The option corresponding with their letter choice
'''
def prompt(prompt_text: str, options: list[str]) -> str:
    #Displays prompt text
    print(prompt_text)
    # Avaliable Letter Choices
    ALC = [] # we want this list to be: ["a", "b"]
    #Displays the options
    for index in range(len(options)):
        # print(index)
        letter: str = LETTERS[index]
        ALC.append(letter)
        option: str = options[index]
        print(f"\t{letter}. {option}")
    print(ALC)
    response: str = input("Type a letter: ")
    response = response.lower() #Makes the letters in the response in lower case
    if len(response) > 1:
        print("Response is too long!")
    elif response not in LETTERS:
        print("Response is not a letter!")
    elif response not in ALC:
        print("Choices have to be either: A or B!")
    index: int = ALC.index(response) # Converts their letter choice into the number of their choice (which is a valid index of the options list)
    chosen_option: str = options[index] # Converts from index to the option that was chosen by the player 
    return chosen_option

if __name__ == "__main__":
    # put prompt testing code in this if block
    choice = prompt("Where would you like to start?", ["Pitcher, OK", "Barrington, IL", "Cupertino, CA"])
    print(choice)
else:
    pass