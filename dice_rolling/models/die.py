from random import Random


class Die:
    rand = Random()

    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return self.rand.randint(1, self.sides)
