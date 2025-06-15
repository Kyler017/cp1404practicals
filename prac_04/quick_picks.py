import random
MAX_NUMBERS = 45
MIN_NUMBERS = 1
number_of_lines = 6

def main():
    """Quick picks program - choose sets of random numbers."""
    number_of_quick_picks = int(input("How many quick picks? "))
    while number_of_quick_picks < 0:
        print("That makes no sense!")
        number_of_quick_picks = int(input("How many quick picks? "))

    for i in range(number_of_quick_picks):
        quick_pick = []
        for j in range(number_of_lines):
            number = random.randint(MIN_NUMBERS, MAX_NUMBERS)
            while number in quick_pick:
                number = random.randint(MIN_NUMBERS, MAX_NUMBERS)
            quick_pick.append(number)
        quick_pick.sort()
        # the following uses a generator expression (like a list comprehension)
        # to format each number in quick_pick in the same way
        # this is then turned into a single string with the join method
        print(" ".join(f"{number:2}" for number in quick_pick))


main()