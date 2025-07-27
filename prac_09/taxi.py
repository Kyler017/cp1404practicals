"""
CP1404/CP5632 Practical
Specialised Taxi class based on Car class, with fare calculation.
"""
from car import Car


class Taxi(Car):

    price_per_km = 1.23  # Add a class variable shared by all Taxi objects

    def __init__(self, name, fuel):
        super().__init__(name, fuel)
        self.current_fare_distance = 0


