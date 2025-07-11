from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""

    my_car = Car("MyCar", 180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)

    limo = Car("Limo", 100)

    limo.add_fuel(20)

    print(f"Limo has fuel: {limo.fuel}")

    limo.drive(115)

    print(limo)


main()


