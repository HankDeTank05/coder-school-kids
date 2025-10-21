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
circle_drawer.hide_turtle()
wave_drawer.hide_turtle()
circle_drawer.speed(0)
wave_drawer.speed(0)
circle_drawer.pensize(2)
wave_drawer.pensize(2)
circle_drawer.color("white")
wave_drawer.color("cyan")

# parameters
NUM_TERMS = 10
BASE_RADIUS = 75
time_step = 0
wave_points = []

# turn off autorefresh
screen = turtle.Screen()
screen.tracer(0)

while True:
    circle_drawer.clear()
    wave_drawer.clear()

    x, y = -300, 0
    circle_drawer.penup()
    circle_drawer.goto(x, y)
    circle_drawer.pendown()
    
