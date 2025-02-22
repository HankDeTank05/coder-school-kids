import pgzero

class Character:

    def __init__(self):
        self.actor = Actor('character')
        self.actor.pos = 0,0
        self.speed = 10

    def update(self):
        if keyboard[keys.a] == True:
            self.actor.left -= self.speed
        if keyboard[keys.d] == True:
            self.actor.left += self.speed;

    def draw(self):
        self.actor.draw()
