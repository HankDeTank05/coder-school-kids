
def prompt_for_input(prompt: str, options: list[str]) -> str:

    input_is_valid = False

    while not input_is_valid:

        print(prompt)
        for i in range(len(options)):
            print(f"{i+1}. {options[i]}")

        response = input()

        if response.isdecimal():
            choice_index = int(response) - 1
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

prompt_for_input("well exploring the forest you find a portal do you want to enter.",
                 ["yes","no"])



