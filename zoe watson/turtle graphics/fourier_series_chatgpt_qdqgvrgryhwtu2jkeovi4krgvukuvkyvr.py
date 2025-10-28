import turtle
import math
import time

# setup
turtle.setup(1000, 600)
turtle.bgcolor("black")
turtle.colormode(1.0)

# create turtles
circle_drawer = turtle.Turtle()
wave_drawer = turtle.Turtle()
circle_drawer.hideturtle()
wave_drawer.hideturtle()
circle_drawer.speed(0)
wave_drawer.speed(0)
circle_drawer.pensize(2)
wave_drawer.pensize(2)
circle_drawer.color("white")
wave_drawer.color("cyan")

# parameters
NUM_TERMS = 100
BASE_RADIUS = 75
time_step = 0
wave_points = []

# turn off autorefresh
screen = turtle.Screen()
screen.tracer(0)

while True:
    circle_drawer.clear()
    wave_drawer.clear()

    x, y = -300, 0 # starting point for circles
    circle_drawer.penup()
    circle_drawer.goto(x, y)
    circle_drawer.pendown()

    # compute fourier sum
    for n in range(1, NUM_TERMS * 2, 2): # odd armonics: 1, 3, 5....
        radius = (4 / (math.pi * n)) * BASE_RADIUS
        prev_x, prev_y = x, y
        x += radius * math.cos(n * time_step)
        y += radius * math.sin(n * time_step)

        # draw each epicycle
        circle_drawer.color(0.5, 0.5, 0.5)
        circle_drawer.penup()
        circle_drawer.goto(prev_x, prev_y - radius)
        circle_drawer.pendown()
        circle_drawer.circle(radius)
        circle_drawer.penup()
        circle_drawer.goto(prev_x, prev_y)
        circle_drawer.pendown()
        circle_drawer.color("white")
        circle_drawer.goto(x, y)

    # draw the wave being formed
    wave_points.insert(0, (x, y))
    wave_drawer.penup()
    wave_drawer.goto(200, wave_points[0][1])
    wave_drawer.pendown()
    for i in range(1, len(wave_points)):
        wave_drawer.goto(200 + i, wave_points[i][1])

    # trim the list to prevent overflow
    if len(wave_points) > 600:
        wave_points.pop()

    # draw connection line
    circle_drawer.color("yellow")
    circle_drawer.goto(200, y)

    screen.update()
    time.sleep(0.02)
    time_step += 0.05
