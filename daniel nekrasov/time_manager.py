
class TimeManager:
    
    #constructor
    def __init__(self):
        self._timescale = 1

    # TODO: write a function to get the timescale value
    def get_timescale(self):
        return self._timescale
     
    # TODO: write a function to set the timescale value
    def set_timescale(self, new_timescale):
        assert(new_timescale > 0) # crash the game if someone tries to set a timescale 0 (freeze time) or <0 (reverse time)
        self._timescale = new_timescale