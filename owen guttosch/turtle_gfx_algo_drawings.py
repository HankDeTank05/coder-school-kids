import time
import turtle as *

def stars(line_color, fill_color, direction, length):
    color(line_color)
    fillcolor(fill_color)
    begin_fill()
    while True:
        forward(length)
        left(direction)
        if abs(pos()) < 1:
            break
    end_fill()

for angle in range(90, 180):
    print(angle)
    reset()
    stars('green', 'yellow', angle, 150)
    time.sleep(1)
