"""
CP1404/CP5632 Practical
Testing code using assert and doctest

Estimate: 20 minutes
Actual: 18 minutes
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    repeated = [s for i in range(n)]
    return " ".join(repeated)


def is_long_word(word, length=5):
    return len(word) >= length


def format_sentence(phrase):
    if phrase == "":
        return "."

    formatted = phrase.strip()
    sentence = formatted[0].upper() + formatted[1:]
    if not sentence.endswith("."):
        sentence += "."
    return sentence


def run_tests():
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    car = Car()
    assert car._odometer == 0, "Car does not set odometer correctly"

    car = Car(fuel=10)
    assert car.fuel == 10, "Car fuel should be 10"

    another_car = Car()
    assert another_car.fuel == 0, "Car default fuel should be 0"


run_tests()

doctest.testmod()
