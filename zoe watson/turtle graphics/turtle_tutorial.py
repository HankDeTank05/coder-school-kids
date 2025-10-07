from turtle import *

def colors_of_ROYGBV(colors):
    for steps in range(100):
        for c in colors :
            color(c)
            forward(steps)
            right(30)

def star(line_color, fill_color):
    color(line_color)
    fillcolor(fill_color)
    begin_fill()
    while True:
        forward(200)
        left(100)
        if abs (pos()) < 1:
            break
    end_fill()
