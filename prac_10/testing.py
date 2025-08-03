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


