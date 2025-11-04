import turtle
import random
import math
import sys

# --- setup ---
screen = turtle.Screen()
screen.title("Fractal Visualizations")
screen.setup(width=900, height=700)
screen.bgcolor("black")
turtle.colormode(255)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.penup()

# utility: random brighter color
def rand_color():
    return (random.randint(60, 255), random.randint(60, 255), random.randint(60, 255))

# --- sierpinski triangle ---
def draw_filled_triangle(t, p1, p2, p3, color):
    t.fillcolor(color)
    t.penup()
    t.goto(p1)
    t.pendown()
    t.begin_fill()
    t.goto(p2)
    t.goto(p3)
    t.goto(p1)
    t.end_fill()

def midpoint(a, b):
    return ((a[0] + b[0]) / 2.0, (a[1] + b[1]) / 2.0)

def sierpinski(t, order, p1, p2, p3):
    if order == 0:
        draw_filled_triangle(t, p1, p2, p3, rand_color())
    else:
        # three sub-triangles
        m12 = midpoint(p1, p2)
        m23 = midpoint(p2, p3)
        m31 = midpoint(p3, p1)
        sierpinski(t, order - 1, p1, m12, m31)
        sierpinski(t, order - 1, m12, p2, m23)
        sierpinski(t, order - 1, m31, m23, p3)

def run_sierpinski(order=5):
    pen.clear()
    pen.speed(0)
    size = 600
    # big triangle vertices centered
    top = (0, size * 0.33)
    left = (-size / 2, -size * 0.5)
    right = (size / 2, -size * 0.5)
    sierpinski(pen, order, left, right, top)
    pen.hideturtle()

# ---Koch Snowflake ---
def koch(t, order, length):
    if order == 0:
        t.pendown()
        t.forward(length)
    else:
        koch(t, order - 1, length/3)
        t.left(60)
        koch(t, order - 1, length/3)
        t.right(120)
        koch(t, order - 1, length/3)
        t.left(60)
        koch(t, order - 1, length/3)

def run_koch(order=4):
    pen.clear()
    pen.penup()
    pen.goto(-300, 50)
    pen.setheading(0)
    pen.pensize(2)
    pen.pencolor(rand_color())
    pen.speed(0)
    pen.pendown()
    for _ in range(3):
        koch(pen, order, 600)
        pen.right(120)

# --- fractal tree ---
def fractal_tree(t, branch_len, angle, factor, depth):
    if depth == 0 or branch_len < 4:
        return
    # set color based on depth
    color = (min(int(50 + 200 * depth / 8), 255), max(int(20 + 120 * (8 - depth) / 8), 0), int(80 + 160 * (8 - depth) / 8))
    t.pencolor(color)
    t.pensize(max(1, depth))
    t.pendown()
    t.forward(branch_len)
    # save position
    pos = t.position()
    heading = t.heading()

    # left branch
    t.left(angle + random.uniform(-6, 6))
    fractal_tree(t, branch_len * factor * (0.9 + random.uniform(-0.05, 0.05)), angle, factor, depth - 1)

    # restore and right branch
    t.penup()
    t.setposition(pos)
    t.setheading(heading)
    t.pendown()
    t.right(angle + random.uniform(-6, 6))
    fractal_tree(t, branch_len * factor * (0.9 + random.uniform(-0.05, 0.05)), angle, factor, depth - 1)

    # return to trunk end and go back
    t.penup()
    t.setposition(pos)
    t.setheading(heading)
    t.backward(branch_len)
    t.pendown()

def run_tree():
    pen.clear()
    pen.penup()
    pen.goto(0, -300)
    pen.setheading(90)
    pen.pensize(8)
    pen.pencolor((120, 70, 30))
    pen.speed(0)
    pen.pendown()
    # trunk
    pen.forward(80)
    # move to trunk-top for recursion
    pen.penup()
    pen.forward(0)
    pen.pendown()
    #recursion start from trunk-top
    fractal_tree(pen, branch_len=120, angle=40, factor=0.9, depth=9)
    pen.hideturtle()

# run_sierpinski()
# run_koch()
run_tree()
