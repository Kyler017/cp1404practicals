from guitar import Guitar


def load_guitars(filename):
    guitar_collection = [ ]
    with open(filename, 'r') as file:
        for line in file:
            name, year, cost = line.strip().split(',')
            guitar_collection.append(Guitar(name, int(year), float(cost)))
    return guitar_collection


def display_guitars(guitars):
    for guitar in guitars:
        print(f"{guitar.name}, {guitar.year}, ${guitar.cost:.2f}")


def add_new_guitar(guitars):
    name = input("Enter guitar name (or blank to stop): ")
    while name:
        year = int(input("Enter year: "))
        cost = float(input("Enter cost: "))
        guitars.append(Guitar(name, year, cost))
        name = input("Enter guitar name (or blank to stop): ")


def save_guitars(filename, guitars):
    file = open(filename, 'w')
    for guitar in guitars:
        file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


def main():
    filename = "guitars.csv"
    guitars = load_guitars(filename)

    print("All guitars:")
    display_guitars(guitars)

    guitars.sort()
    print("\nGuitars sorted by year: ")
    display_guitars(guitars)

    print("\nAdd your guitars:")
    add_new_guitar(guitars)

    save_guitars(filename, guitars)
    print("\nGuitars saved to", filename)


if __name__ == "__main__":
    main()