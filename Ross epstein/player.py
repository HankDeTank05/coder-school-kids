from common import *

class Player:

    def __init__(self):
        self._max_hp = STARTING_HP
        self._hp = self._max_hp
        self._weapon = None
        self._inventory = []
        self._money = STARTING_MONEY
        self._armor = None
        self._alignment = STARTING_ALIGNMENT

    def change_alignment(self, alignment_delta: int) -> None:
        self._alignment += alignment_delta
        if self._alignment < MAX_EVIL:
            self._alignment = MAX_EVIL
        elif self._alignment > MAX_GOOD:
            self._alignment = MAX_GOOD
