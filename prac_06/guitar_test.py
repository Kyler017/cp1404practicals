from guitar import Guitar

def main():
    current_year = 2025

    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    expected_age1 = current_year - 1922
    print(f"{guitar1.name} get_age() - Expected {expected_age1}. Got {guitar1.get_age()}")
    print(f"{guitar1.name} is_vintage() - Expected True. Got {guitar1.is_vintage()}")

    guitar2 = Guitar("Another Guitar", 2013, 1000)
    expected_age2 = current_year - 2013
    print(f"{guitar2.name} get_age() - Expected {expected_age2}. Got {guitar2.get_age()}")
    print(f"{guitar2.name} is_vintage() - Expected False. Got {guitar2.is_vintage()}")

main()