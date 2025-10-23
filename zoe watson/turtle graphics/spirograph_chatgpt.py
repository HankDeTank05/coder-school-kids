import turtle
import random

# set up the turtle
t = turtle.Turtle()
t.speed(0) # fastest drawing speed
turtle.bgcolor("black") # makes bright colors look better
t.width(2)

# function to pick a random color
def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)

color_num = 0x000000

turtle.colormode(1.0) # allows rgb colors between 0 and 1

# draw the spirograph
for radius in range(60, 150,10):
    for angle in range(0, 360, 5):
        t.pensize(1)
        t.color(f"#{color_num}")
        t.setheading(angle)
        t.circle(radius)
        t.right(20)
        color_num += 1

turtle.done()
