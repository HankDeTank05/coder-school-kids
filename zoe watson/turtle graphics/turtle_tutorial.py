from turtle import *

def colors_of_ROYGBV(colors):
    for steps in range(100):
        for c in colors :
            color(c)
            forward(steps)
            right(30)

def star(line_color, fill_color, angle):
    color(line_color)
    fillcolor(fill_color)
    start_x = round(xcor(), 3)
    start_y = round(ycor(), 3)
    print(f"started at {start_x},{start_y}")
    begin_fill()
    while True:
        forward(200)
        left(angle)
        if round(xcor(), 3) == start_x and round(ycor(), 3) == start_y:
            break
    end_fill()

def stars(star_count):
    forward(200 * ((star_count/2)-1))
    for s in range(star_count):
        star('black', 'indigo', 144)
        backward(200)

reset()
