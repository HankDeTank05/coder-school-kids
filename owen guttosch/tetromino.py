import pgzrun

'''imports
the
class
'''
from block import Block

class Tetromino:

    # constructor
    def __init__(self, blocks4: list[Block]):
        self.blocks4: list[Block] = blocks4

    def draw_the_thingimagiggie(self):
        for block in self.blocks4:
            block.draw()

WIDTH = 360
HEIGHT = 240

BLOCKCOLORANDSTUFF = (15, 72, 94)

myblocks = [
    Block(7, 20, BLOCKCOLORANDSTUFF),
    Block(6, 20, BLOCKCOLORANDSTUFF),
    Block(6, 21, BLOCKCOLORANDSTUFF),
    Block(6, 22, BLOCKCOLORANDSTUFF)
]
my_tetro = Tetromino(myblocks)

def update():
    pass

def draw():
    my_tetro.draw_the_thingimagiggie()

pgzrun.go()

