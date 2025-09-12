import better_math as bm
import circle as cir

class CollisionManager:
    #constructor
    def __init__(self):
        pass

    @staticmethod
    def CheckOneToOne(thing1: cir.Circle, thing2:  cir.Circle):
        if bm.circle_collide(thing1, thing2):
            pass # TODO: come back and implement collision behavior for these things

    @staticmethod
    def CheckOneToMany(thing, many_things: list):
        pass

    @staticmethod
    def CheckManyToMany(many_things1: list , many_things2: list):
        pass