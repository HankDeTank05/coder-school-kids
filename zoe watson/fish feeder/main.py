import pygame
import datetime

pygame.init()


brunch_time = datetime.time(8, 0, 0)
   
linner_time = datetime.time(18,0,0)


def feed_fishy(amount):
    print(f"The fish has been fed {amount} food")

running = True
while running:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False
    
    now = datetime.datetime.now().time()

    if now == brunch_time:
        print("Brunch")
        feed_fishy(1)
 
    elif now == linner_time:
        print("Linner")
        feed_fishy(2)

