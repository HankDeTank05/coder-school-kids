class GameObject:

    #constructor
    def __init__(self, pos, color):
        self.pos = pos
        self.color = color

class Movable(GameObject):

    #constructor
    def __init__(self, pos, color, speed, dir):
        super().__init__(pos, color)
        self.speed = speed
        self.dir = dir


class NonMovable(GameObject):

    # constructor
    def __init__(self, pos, color):
        super().__init__(pos, color)