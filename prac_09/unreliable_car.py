"""
CP1404/CP5632 Practical
Add UnreliableCar subclass of Car, with a chance it won't drive.
"""

import random
from car import Car


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        random_number = random.uniform(0, 100)
        if random_number < self.reliability:
            return super().drive(distance)
        return 0
