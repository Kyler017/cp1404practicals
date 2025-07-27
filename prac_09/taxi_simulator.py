"""
CP1404/CP5632 Practical
Add a menu-based Taxi simulator that shows polymorphism.
"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    current_taxi = None
    total_bill = 0.0

    print("Let's drive!")
    menu = "q)uit, c)hoose taxi, d)rive"
    print(menu)
    user_choice = input(">>> ").lower()

    while user_choice != "q":
        if user_choice == "c":
            current_taxi = choose_taxi(taxis)
        elif user_choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                fare = drive_taxi(current_taxi)
                print(f"Your {current_taxi.name} trip cost you ${fare:.2f}")
                total_bill += fare
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_bill:.2f}")
        print(menu)
        user_choice = input(">>> ").lower()

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis):
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")
    try:
        choice = int(input("Choose taxi: "))
        if 0 <= choice < len(taxis):
            return taxis[choice]
        else:
            print("Invalid taxi choice")
    except ValueError:
        print("Invalid input")
    return None


def drive_taxi(taxi):
    distance = float(input("Drive how far? "))
    taxi.start_fare()
    taxi.drive(distance)
    return taxi.get_fare()


main()
