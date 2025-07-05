"""CP1404/CP5632 Practical - Car class example."""


class Car:

    def __init__(self, name="", fuel=0):
        self.name = name
        self.fuel = fuel
        self._odometer = 0


