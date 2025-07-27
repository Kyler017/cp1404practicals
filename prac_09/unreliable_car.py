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
