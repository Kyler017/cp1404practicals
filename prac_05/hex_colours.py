HEX_COLOURS = {
    "absolute zero": "#0048ba",
    "baby blue": "#89cff0",
    "black": "#000000",
    "white": "#ffffff",
    "blond": "#faf0be",
    "blue green": "#0d98ba",
    "buff": "#f0dc82"
}

def main():
    colour = input("please enter colour name: ")
    while colour != "":
        colour = colour.lower()
        if colour in HEX_COLOURS:
            print(f"{HEX_COLOURS[colour].lower()}")
        else:
            print("you enter the wrong color")
        colour = input("please enter colour name: ")

main()