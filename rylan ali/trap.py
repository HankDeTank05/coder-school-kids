
class Trap:

    def __init__(self):
        self.color = None # dark green
        self.size = None
        self.pos = None
        self.act_rate = None # activation rate (aka, the percent chance the trap will trigger)

    def update(self, frame_time):
        pass

    def draw(self, screen):
        pass