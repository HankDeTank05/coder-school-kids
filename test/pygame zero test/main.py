import pgzrun

from character import Character

WIDTH = 400
HEIGHT = 300

player = Character()

def update():
    player.update()

def draw():
    screen.clear()
    player.draw()

pgzrun.go()
