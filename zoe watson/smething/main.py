import time

import os

import keyboard

snake = "~^vv^~"
snakehead = "U_U"
WIDTH = 50 #Terminal width (ajust it for fun)
pos = 0
direction = 1 # 1 = right, -1 = left

hunger = 10 # 0 = starving 10 = full

last_hunger = time.time()

while True:
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    #FEEDING
    if keyboard.is_pressed("f"):
        hunger = min(10, hunger + 1)

    #Hungry-ness
    if time.time() - last_hunger > 1:
        hunger -= 1
        last_hunger = time.time() 
    
    # Determine mood
    if hunger >= 7:
        mood = "😊 Happy"
    elif hunger >= 4:
        mood = "😐 Getting hungry"
    elif hunger >= 1:
        mood = "😠 Hungry!"
    else:
        mood = "💀 STARVING!"

    #draw snake and stats 
    print("Press F to feed the snake!\n")
    print(" " * pos + snake ) #print snake at it's locaton
    print(f"\nHunger: {hunger}/10  Mood: {mood}")
    
    # update position
    pos += direction

    #bounce at edges
    if pos <= 0 or pos >= WIDTH:
        direction *= -1 

    time.sleep(0.05)