import gameobject as go

class Entity(go.Movable):

    #constructor
    def __init__(self, pos, color, speed, dir):
        super().__init__(pos, color, speed, dir)