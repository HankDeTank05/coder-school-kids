# import turtle

# # --- Setup screen ---
# screen = turtle.Screen()
# screen.bgcolor("skyblue")
# screen.title("Giraffe Drawing with Turtle")

# # --- Create turtle ---
# t = turtle.Turtle()
# t.speed(8)
# t.width(3)
# t.hideturtle()

# # Function to draw filled shapes
# def draw_shape(color, points):
#     t.penup()
#     t.goto(points[0])
#     t.color("black", color)
#     t.begin_fill()
#     t.pendown()
#     for x, y in points[1:]:
#         t.goto(x, y)
#     t.goto(points[0])
#     t.end_fill()

# # --- Draw the giraffe body ---
# draw_shape("#DEB887", [(-50, -100), (50, -100), (70, 50), (-70, 50)])

# # --- Draw the neck ---
# draw_shape("#DEB887", [(40, 50), (80, 250), (20, 250), (-20, 50)])

# # --- Draw the head ---
# draw_shape("#DEB887", [(80, 250), (130, 260), (130, 220), (80, 220)])

# # --- Draw the ears ---
# draw_shape("#DEB887", [(130, 260), (140, 280), (130, 280)])
# draw_shape("#DEB887", [(90, 260), (80, 280), (90, 280)])

# # --- Draw the horns (ossicones) ---
# t.penup()
# t.goto(100, 280)
# t.pendown()
# t.color("brown")
# t.setheading(90)
# t.forward(15)
# t.dot(10, "brown")

# t.penup()
# t.goto(125, 280)
# t.pendown()
# t.setheading(90)
# t.forward(15)
# t.dot(10, "brown")

# # --- Draw spots on the body ---
# t.penup()
# spots = [(-30, 0), (-10, -50), (10, 20), (30, -30), (0, -70)]
# for x, y in spots:
#     t.goto(x, y)
#     t.dot(25, "saddlebrown")

# # --- Draw spots on the neck ---
# spots_neck = [(40, 150), (60, 100), (50, 200), (30, 80)]
# for x, y in spots_neck:
#     t.goto(x, y)
#     t.dot(20, "saddlebrown")

# # --- Draw an eye ---
# t.penup()
# t.goto(115, 240)
# t.pendown()
# t.dot(10, "black")

# # --- Ground ---
# t.penup()
# t.goto(-300, -100)
# t.color("green")
# t.pendown()
# t.begin_fill()
# t.forward(600)
# t.right(90)
# t.forward(50)
# t.right(90)
# t.forward(600)
# t.end_fill()

# # --- Caption ---
# t.penup()
# t.goto(0, -180)
# t.color("black")
# t.write("Giraffe (Turtle Graphics)", align="center", font=("Courier", 14, "bold"))

# turtle.done()
 
import turtle

ANIMATE = False

# --- Setup screen ---
screen = turtle.Screen()
screen.bgcolor("skyblue")
screen.title("Cartoon Giraffe in Turtle Graphics")

# --- Create turtle ---
t = turtle.Turtle()
t.speed(9)
t.width(3)
# t.hideturtle()

if not ANIMATE:
    turtle.tracer(0)

# Helper: draw filled circle
def draw_circle(color, x, y, radius):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.color("black", color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Helper: draw filled oval
def draw_oval(color, x, y, tilt, stretch_wid, stretch_len):
    t.penup()
    t.goto(x, y)
    t.setheading(tilt)
    t.pendown()
    t.color("black", color)
    t.begin_fill()
    for i in range(2):
        t.circle(stretch_wid, 90)
        t.circle(stretch_len, 90)
    t.end_fill()

# --- Body ---
draw_oval("#DEB887", 0, -50, 0, 60, 100)  # light brown body

# --- Legs ---
t.color("black", "#DEB887")
for x in [-40, -20, 20, 40]:
    t.penup()
    t.goto(x, -40)
    t.setheading(-90)
    t.pendown()
    t.begin_fill()
    t.forward(90)
    t.right(90)
    t.forward(15)
    t.right(90)
    t.forward(90)
    t.end_fill()

# Hooves
t.color("black", "saddlebrown")
for x in [-55, -35, 5, 25]:
    t.penup()
    t.goto(x, -130)
    t.setheading(0)
    t.pendown()
    t.begin_fill()
    for _ in range(2):
        t.forward(15)
        t.right(90)
        t.forward(10)
        t.right(90)
    t.end_fill()

# --- Neck ---
t.color("black", "#DEB887")
t.penup()
t.goto(40, 20)
t.pendown()
t.begin_fill()

t.setheading(75)
t.forward(185)

t.setheading(0)
t.forward(30)

t.setheading(253)
t.forward(200)

t.end_fill()
t.penup()

# --- Head ---
draw_oval("#DEB887", 110, 180, 10, 30, 40)

# --- Ears ---
t.color("black", "#DEB887")
for (x, y) in [(130, 210), (95, 210)]:
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.circle(10)
    t.end_fill()

# --- Horns (ossicones) ---
t.color("black", "saddlebrown")
for (x, y) in [(105, 225), (125, 225)]:
    t.penup()
    t.goto(x, y)
    t.setheading(90)
    t.pendown()
    t.begin_fill()
    t.forward(15)
    t.circle(5)
    t.end_fill()

# --- Eye ---
draw_circle("black", 125, 190, 5)

# --- Spots ---
t.color("saddlebrown")
spots = [
    (-30, 0), (0, -20), (30, 10),
    (50, -40), (-40, -30), (60, 120),
    (50, 70), (35, 150)
]
for (x, y) in spots:
    draw_circle("saddlebrown", x, y, 10)

# --- Tail ---
t.penup()
t.goto(-100, 55)
t.setheading(200)
t.pendown()
t.width(4)
t.color("saddlebrown")
t.forward(50)
t.dot(10, "saddlebrown")

# # --- Ground ---
# t.penup()
# t.goto(-300, -130)
# t.color("forestgreen")
# t.pendown()
# t.begin_fill()
# t.setheading(0)
# t.forward(600)
# t.right(90)
# t.forward(50)
# t.right(90)
# t.forward(600)
# t.end_fill()

# --- Caption ---
t.penup()
t.goto(0, -190)
t.color("black")
t.write("Cartoon Giraffe 😒 (Turtle Graphics)", align="center", font=("Courier", 14, "bold"))

if not ANIMATE:
    turtle.update()

turtle.done()
