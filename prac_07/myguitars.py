from guitar import Guitar


def load_guitars(filename):
    guitar_collection = [ ]
    with open(filename, 'r') as file:
        for line in file:
            name, year, cost = line.strip().split(',')
            guitar_collection.append(Guitar(name, int(year), float(cost)))
    return guitar_collection


