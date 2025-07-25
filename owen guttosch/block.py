import pgzrun

class Block:
 
    # constructor
    def __init__(self, grid_x: int, grid_y: int, color: tuple):
        self.x: int = grid_x
        self.y: int = grid_y
        self.color:      tuple =color
        self.rect: Rect = Rect((self.x, self.y), ())
        '''#shift-3'''

    def __repr__(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass
