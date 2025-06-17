import prompt as p

'''
text-based adventure game in the style of oregon trail
the adventure the player goes on will be based on the game of life (board game)

essential game functions
- Answer questions 
    based on those answers the game will choose a certain path for player to follow
    1. prompt player with question
    2. Wait for the answer
    3. Process the response

NEXT TIME:
1. DONE: write code for basic prompt and response processing
2. write code to create the data structure for a tree
'''

if __name__ == "__main__":
    q1_options: list[str] = ["Pitcher, OK", "Barrington, IL"]
    q1_choice: str = p.prompt("Where would you like to start?", q1_options)
    q2_prompt: str = "Where would you like to live?"
    q2_options: list[str] = []

    if q1_choice == q1_options[0]: # Did the player pick Pitcher Ok?
        q2_options.append("At the top of a mountain")
        q2_options.append("At the base of a mountain")
    elif q1_choice == q1_options[1]: # If not, did the player pick Barrington, IL?
        q2_options.append("Next to a lake")
        q2_options.append("In the middle of dense forest")
    
    q2_choice: str = p.prompt(q2_prompt, q2_options)
