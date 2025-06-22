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


