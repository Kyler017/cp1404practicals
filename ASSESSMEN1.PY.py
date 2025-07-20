"""
Name: KAN YIJIE
Date started: 19/06/2025
GitHub URL: https://github.com/cp1404-students/a1-movies-Kyler017
"""

FILENAME = "movies.csv"
VALID_CATEGORIES = ["Action", "Comedy", "Documentary", "Drama", "Thriller", "Other"]
UNWATCHED = "u"
WATCHED = "w"
MENU_CHOICE = ["D", "A", "W", "Q"]


def main():
    print("Must-See Movies 1.0 - by KAN YIJIE")
    movies = load_movies(FILENAME)
    print(f"{len(movies)} movies loaded from {FILENAME}")

    menu_choice = " "
    while menu_choice != "Q":
        print("Menu:")
        print("D - Display movies")
        print("A - Add new movie")
        print("W - Watch a movie")
        print("Q - Quit")
        menu_choice = input(">>> ").strip().upper()
        if menu_choice not in MENU_CHOICE:
            print("Invalid menu choice")
            continue
        if menu_choice == "D":
            display_movies(movies)
        elif menu_choice == "A":
            add_movie(movies)
        elif menu_choice == "W":
            watch_movie(movies)
        elif menu_choice == "Q":
            save_movies(FILENAME, movies)
            print(f"{len(movies)} movies saved to {FILENAME}")
            print("Have a nice day :)")
            menu_choice = "Q"


def load_movies(filename):
    movies = []
    try:
        with open(filename, "r", encoding="utf-8") as in_file:
            for line in in_file:
                parts = line.strip().split(",")
                title, year, category, status = parts
                movies.append([title, int(year), category, status])
    except FileNotFoundError:
        print(f"Warning: {filename} not found. Starting with an empty list.")
        response = input("Would you like to create a new file? (y/n): ").strip().lower()
        if response == "y":
            save_movies(filename, movies)
    return movies


def save_movies(filename, movies):
    with open(filename, "w", encoding="utf-8") as out_file:
        for movie in movies:
            print(f"{movie[0]},{movie[1]},{movie[2]},{movie[3]}", file=out_file)


def display_movies(movies):
    sorted_movies = sorted(movies, key=lambda x: (x[1], x[0]))
    watched_count = sum(1 for movie in sorted_movies if movie[3] == WATCHED)
    to_watch_count = len(sorted_movies) - watched_count

    for index, movie in enumerate(sorted_movies, 1):
        marker = "*" if movie[3] == UNWATCHED else " "
        print(f"{index:2}. {marker} {movie[0]:<35} - {movie[1]:4} ({movie[2]})")
    print(f"{watched_count} movies watched. {to_watch_count} movies still to watch.")


def add_movie(movies):
    title = get_non_empty_string("Title: ")
    year = get_positive_integer("Year: ")
    print(f"Categories available: {', '.join(VALID_CATEGORIES)}")
    category = get_valid_category("Category: ")
    movies.append([title, year, category, UNWATCHED])
    print(f"{title} ({category} from {year}) added to movie list")


def watch_movie(movies):
    unwatched_movies = [movie for movie in movies if movie[3] == UNWATCHED]
    if not unwatched_movies:
        print("No more movies to watch!")
        return

    print("Enter the movie number to mark watched.")
    sorted_movies = sorted(movies, key=lambda x: (x[1], x[0]))
    while True:
        try:
            choice = int(input(">>> "))
            if choice < 1:
                print("Number must be >= 1")
            elif choice > len(sorted_movies):
                print("Invalid movie number.")
            else:
                selected_movie = sorted_movies[choice - 1]
                selected_movie[3] = WATCHED
                print(f"{selected_movie[0]} ({selected_movie[1]}) watched.")
                break
        except ValueError:
            print("Invalid input; enter a valid number")


def get_non_empty_string(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input can not be blank")


def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 1:
                return value
            print("Number must be >= 1")
        except ValueError:
            print("Invalid input; enter a valid number")


main()