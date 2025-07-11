COUNTRIES_LIST_LOCATION = 1
PLAYERS_LIST_LOCATION = 2



def main():
    filename = "wimbledon.csv"
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        players = []
        next(in_file)
        for line in in_file:
            line = line.strip()
            parts = line.split(",")
            players.append([parts[COUNTRIES_LIST_LOCATION], parts[PLAYERS_LIST_LOCATION]])

        players_dict = champions_input(players)
        countries_list = count_countries(players)

        print_results(players_dict, countries_list)


# turn the list into a dictionary
def champions_input(players):
    players_dict = {}
    for player in players:
        if player[1] in players_dict:
            players_dict[player[1]] += 1
        else:
            players_dict[player[1]] = 1

    return players_dict


def count_countries(players):
    countries = set(player[0] for player in players)
    return sorted(countries)


def print_results(players_dict, countries_list):
    print("Wimbledon champions")
    for player in players_dict:
        print("{}: {}".format(player, players_dict[player]))

    print("\nCountries of champions")
    print(','.join(countries_list))


main()