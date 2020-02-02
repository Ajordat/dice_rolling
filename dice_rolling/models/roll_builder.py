import random

from dice_rolling import Die


class RollBuilder:
    def __init__(self, seed=None):
        self.__n_dice = 1
        self.__n_sides = 0
        self.__rolls = []
        self.__addition = 0
        self.__keep = 0

        Die.rand = random.Random(seed)

    def set_amount_of_dice(self, n_dice):
        self.__n_dice = n_dice

    def set_number_of_sides(self, n_sides):
        self.__n_sides = n_sides

    def addition_to_roll(self, value):
        self.__addition += value

    def keep_n(self, value):
        if abs(value) <= self.__n_dice:
            self.__keep = value

    def build(self):
        self.__rolls = []
        for i in range(self.__n_dice):
            self.__rolls.append(
                Die(self.__n_sides).roll() + self.__addition
            )

    def get_result(self):

        if self.__keep:
            sort = sorted(self.__rolls, reverse=self.__keep > 0)
            return sort[:self.__keep], sort[self.__keep:]

        return self.__rolls
