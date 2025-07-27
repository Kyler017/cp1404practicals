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

    def __str__(self):
        return (f"{super().__str__()}, {self.current_fare_distance}km on current fare, "
                f"${self.price_per_km:.2f}/km")

    def get_fare(self):
        return self.current_fare_distance * self.price_per_km

    def start_fare(self):
        self.current_fare_distance = 0

    def drive(self, distance):
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven
