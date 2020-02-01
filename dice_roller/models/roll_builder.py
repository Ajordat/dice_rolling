from dice_roller import Dice


class RollBuilder:
    def __init__(self, seed=None):
        self.__n_dices = 0
        self.__n_sides = 0
        self.__seed = seed
        self.__rolls = []

    @property
    def _seed(self):
        if self.__seed:
            self.__seed += 1
            return self.__seed

    def set_number_of_dices(self, n_dices):
        self.__n_dices = n_dices

    def set_number_of_sides(self, n_sides):
        self.__n_sides = n_sides

    def build(self):
        self.__rolls = []
        for i in range(self.__n_dices):
            self.__rolls.append(Dice(self.__n_sides, seed=self._seed).roll())

    def get_result(self):
        return self.__rolls
