# import turtle
# import math

# # --- Setup screen ---
# screen = turtle.Screen()
# screen.bgcolor("black")
# screen.title("NASA Logo (Simplified)")

# # --- Create turtle ---
# nasa = turtle.Turtle()
# nasa.speed(10)
# nasa.hideturtle()

# # --- Draw the blue circle (background) ---
# nasa.penup()
# nasa.goto(0, -150)
# nasa.pendown()
# nasa.color("blue")
# nasa.begin_fill()
# nasa.circle(150)
# nasa.end_fill()

# # --- Draw the red vector (simplified) ---
# nasa.penup()
# nasa.goto(-140, 0)
# nasa.pendown()
# nasa.color("red")
# nasa.width(10)
# nasa.setheading(60)
# nasa.circle(200, 60)
# nasa.right(120)
# nasa.circle(-200, 60)
# nasa.penup()

# # --- Draw white orbit line ---
# nasa.goto(-100, 50)
# nasa.pendown()
# nasa.color("white")
# nasa.width(2)
# nasa.setheading(20)
# for i in range(100):
#     nasa.forward(3)
#     nasa.right(1)

# # --- Write NASA text ---
# nasa.penup()
# nasa.goto(-70, -20)
# nasa.color("white")
# nasa.write("N   A   S   A", font=("Arial", 24, "bold"))

# # --- Finish ---
# nasa.penup()
# nasa.goto(0, -200)
# nasa.color("white")
# nasa.write("Simplified NASA Logo", align="center", font=("Courier", 10, "italic"))

# turtle.done()

import turtle
import math
import random

# --- Setup screen ---
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("NASA Logo (More Accurate)")

# --- Create turtle ---
nasa = turtle.Turtle()
nasa.hideturtle()
nasa.speed(0)

# --- Draw blue circular background ---
nasa.penup()
nasa.goto(0, -180)
nasa.pendown()
nasa.color("#0B3D91")  # NASA blue
nasa.begin_fill()
nasa.circle(180)
nasa.end_fill()

# --- Draw white orbit ---
nasa.penup()
nasa.goto(-120, 30)
nasa.pendown()
nasa.color("white")
nasa.width(2)
nasa.setheading(25)
for _ in range(150):
    nasa.forward(4)
    nasa.right(1)

# --- Draw red vector swoosh (stylized) ---
nasa.penup()
nasa.goto(-170, -60)
nasa.setheading(70)
nasa.pendown()
nasa.color("red")
nasa.width(18)

# Main red swoosh curve
nasa.circle(200, 50)
nasa.right(120)
nasa.circle(-200, 55)

# Add small tail
nasa.penup()
nasa.goto(50, 150)
nasa.setheading(-110)
nasa.pendown()
nasa.width(10)
nasa.circle(100, 30)

# --- Add white stars ---
nasa.color("white")
for _ in range(25):
    nasa.penup()
    x = random.randint(-150, 150)
    y = random.randint(-150, 150)
    nasa.goto(x, y)
    nasa.dot(random.choice([2, 3, 4]))

# --- Draw “NASA” text (stylized approximation) ---
nasa.penup()
nasa.goto(-110, -40)
nasa.color("white")
nasa.write("N", font=("Arial", 48, "bold"))

nasa.goto(-35, -40)
nasa.write("A", font=("Arial", 48, "bold"))

nasa.goto(35, -40)
nasa.write("S", font=("Arial", 48, "bold"))

nasa.goto(100, -40)
nasa.write("A", font=("Arial", 48, "bold"))

# --- Optional caption ---
nasa.goto(0, -230)
nasa.color("white")
nasa.write("NASA 'Meatball' Logo (Turtle Approximation)",
           align="center", font=("Courier", 10, "italic"))

turtle.done()
