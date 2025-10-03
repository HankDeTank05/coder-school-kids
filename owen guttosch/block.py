import pgzrun

class Block:
 
    # constructor
    def __init__(self, grid_x: int, grid_y: int, color: tuple):
        self.x: int = grid_x
        self.y: int = grid_y
        self.color:      tuple =color
        self.rect: Rect = Rect((self.x, self.y), (10, 10))
        '''#shift-3'''

    def __repr__(self):
        pass

    def update(self):
        pass

    def draw(self):
        screen.draw.filled_rect(self.rect, self.color)
        screen.draw.rect(self.rect, (238, 230, 0))

'''    
WIDTH = 360
HEIGHT = 240

my_block = Block(grid_x=7, grid_y=12, color=(15, 72, 94))
print(my_block.x)
print(my_block.y)
print(my_block.color)

def update():
    my_block.update()

def draw():
    my_block.draw()

pgzrun.go()
'''
