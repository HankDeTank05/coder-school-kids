# this function returns text of choosen option
def prompt_for_input(prompt: str, options: list[str]) -> str:

    input_is_valid = False

    while not input_is_valid:

        # print prompt
        print(prompt)

        # List options with numbers
        for i in range(len(options)):
            print(f"{i+1}. {options[i]}")

        # let the user input
        response = input()

        # checks if response is a number
        if response.isdecimal():

            # concert response from str to int and reducing it by one
            choice_index = int(response) - 1

            # checks if resposns is valid
            if 0 <= choice_index < len(options):
                chosen_option = options[choice_index]
                # print(f"the index you chose was {choice_index}")
                # print(chosen_option)
                input_is_valid = True
            elif choice_index < 0:
                print("INVAILD OPTION: NUMBER TOO SMALL")
            else:
                print("INVAILD OPTION: NUMBER TOO LARGE")
        else:
            print("INVAILD OPTION: MUST BE ONE OF LISTED NUMBERS")

    return chosen_option

# this function returns a number repersenting a change in alignment
def moral_choice(prompt: str, choice_evil: str, choice_neutral: str, choice_good: str) -> float:
    while True: 
        print(prompt)
        print(f"[Good] {choice_good}")
        print(f"[Neutral] {choice_neutral}")
        print(f"[Evil] {choice_evil}")
        response = input("Enter first letter of word or whole word: ")
        response = response.lower()

        if response == "g" or "good":
            return 1.0
        elif response == "n" or "neutral":
            return 0.0
        elif response == "e" or "evil":
            return -1.0