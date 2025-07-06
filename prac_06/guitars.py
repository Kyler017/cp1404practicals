"""
Estimate: 20 minutes
Actual: 29 minutes
"""

from guitar import Guitar

FILENAME = "guitars.csv"

def main():
    guitars = load_guitars(FILENAME)

    print("My guitars!")
    for guitar in guitars:
        print(guitar)

    print("\nAdd new guitars:")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitars.append(Guitar(name, year, cost))
        name = input("Name: ")

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar}")

    save_guitars(FILENAME, guitars)


def load_guitars(filename):
    guitars = []
    try:
        with open(filename, "r") as in_file:
            for line in in_file:
                parts = line.strip().split(",")
                name = parts[0]
                year = int(parts[1])
                cost = float(parts[2])
                guitars.append(Guitar(name, year, cost))
    except FileNotFoundError:
        print(f"{filename} not found. Starting with an empty list.")
    return guitars



