"""
CP1404/CP5632 Practical
Test the Taxi class with basic usage.
"""

from taxi import Taxi

def main():
    my_taxi = Taxi("Prius 1", 100)
    my_taxi.drive(40)
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")

    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)
    print(f"Current fare after 100km: ${my_taxi.get_fare():.2f}")

main()
