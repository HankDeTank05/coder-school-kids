import pgzrun

WIDTH = 800
HEIGHT = 600

cybertruck = Actor('cybertruck_25_left')
cybertruck.pos = WIDTH/2, HEIGHT/2

background_move = 0

building = Rect((WIDTH/2, HEIGHT/2), (50, 200))

'''
IDEAS
- make a road for it to drive on
- have it pass villages every so often
- it's an uber, so it stops to pick up people
- put music in
'''

def on_key_down(key):
    global background_move
    if keyboard[keys.LEFT]:
        cybertruck.image = 'cybertruck_25_left'
        background_move = 1
    if keyboard[keys.RIGHT]:
        cybertruck.image = 'cybertruck_25_right'
        background_move = -1

def on_key_up(key):
    global background_move
    if keyboard[keys.LEFT]:
        background_move = 0
    if keyboard[keys.RIGHT]:
        background_move = 0

def update():
    building.move_ip(background_move, 0)

def draw():
    screen.clear()
    screen.draw.rect(building, (128, 128, 128))
    cybertruck.draw()

pgzrun.go()