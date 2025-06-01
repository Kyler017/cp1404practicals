MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""

def main():
    """ Celsius to Fahrenheit and Fahrenheit to Celsius """
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = celsiusfahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            # TODO: Write this section to convert F to C and display the result
            fahrenheit = float(input("Celsius: "))
            celsius = fahrenheitcelsius(fahrenheit)
            print(f"Result: {celsius:.2f} F")
            pass
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

def celsiusfahrenheit(celsius):
    return celsius * 9.0 / 5 + 32


