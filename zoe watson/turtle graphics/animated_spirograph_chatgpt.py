import turtle
import random
import math
import time

#Setup
t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
t.width(2)
turtle.colormode(1.0)

def random_color():
    return(random.random(), random.random(), random.random())

angle = 0
radius = 100

# Hide turtle mouse thing foa cleaner animation.
t.hideturtle()

radius_delta = 0
radius_variance = 3

#Animate continuously
while True:
    t.color(random_color())
    t.setheading(angle)
    t.circle(radius)
    angle += 10                  #change this for a faster/slower rotation
    #radius = 80 + 40 * math.sin(angle * math.pi / 180) #oscillate radius for variety
    radius += random.randint(radius_delta - radius_variance, radius_delta + radius_variance)

    
    #slight pause for smooth animation
    time.sleep(0.02)

    # gradually fade old drawings
    t.getscreen().tracer(0) # temporarily stop auto-referesh
    fade = turtle.Turtle()  # make a transparent overlay
    fade.hideturtle()
    fade.speed(0)
    fade.color(0, 0, 0)
    fade.penup()
    fade.goto(-400, -400)
    fade.begin_fill()
    for _ in range(4):
        fade.forward(800)
        fade.left(90)
    fade.end_fill()
    fade.penup()
    fade.clear()   # clear the overlay to keep it light
    t.getscreen().update()    # update with a fading effect
