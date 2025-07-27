"""
CP1404/CP5632 Practical
Band class to show aggregation: Band has Musicians.
"""


class Band:

    def __init__(self, name=""):
        self.name = name
        self.musicians = []

    def add(self, musician):
        self.musicians.append(musician)

    def __str__(self):
        musician_strings = ", ".join(str(m) for m in self.musicians)
        return f"{self.name} ({musician_strings})"

