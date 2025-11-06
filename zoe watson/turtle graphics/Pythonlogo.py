import turtle

t = turtle.Turtle()
t.speed(10)
turtle.bgcolor("#1E1E1E")
t.pensize(3)

def draw_snake(color, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(50, 180)
    t.forward(80)
    t.circle(50, 180)
    t.forward(80)
    t.end_fill()

# Draw top (yellow)
draw_snake("#FFD43B", -30, 0)

# Draw bottom (blue)
draw_snake("#306998", 30, -80)

# Draw eyes
t.penup()
t.goto(-10, 60)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(5)
t.end_fill()

t.penup()
t.goto(70, -20)
t.pendown()
t.begin_fill()
t.circle(5)
t.end_fill()

t.hideturtle()
turtle.done()
