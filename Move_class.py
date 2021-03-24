# Move Class

from Pokemon_class import *
from secondary_effect import *

class Move:
    def __init__(self, name, typing, category, power, accuracy):
        self.typing = typing
        self.category = category
        self.power = power
        self.accuracy = accuracy
