import pgzrun

WIDTH=1920
HEIGHT=1080
 
WIDTH = 1280
HEIGHT = 720

#chicken banana
flappy=Actor('flappy')
flappy.pos = 100, 358

def on_key_down(key):
    if key==UP:
        pass

def update():
    pass

def draw():
    screen.clear()
    flappy.draw()

pgzrun.go()