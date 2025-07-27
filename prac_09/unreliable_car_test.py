"""
CP1404/CP5632 Practical
Test UnreliableCar drive logic with randomness.
"""

from unreliable_car import UnreliableCar


def main():
    unreliable = UnreliableCar("BadCar", 100, 30)
    total_driven = 0
    attempts = 100

    for i in range(attempts):
        distance = unreliable.drive(1) 
        total_driven += distance

    print(f"Tried to drive {attempts} km. Actually drove: {total_driven} km")
    print("Expected: Around 30 km (give or take, because of randomness)")


main()
