"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random
def main():
    score = float(input("Enter score: "))
    print(student_socre(score))
    random_number = random.randint(0,100)
    print(f"score: {score:.f}")
    print(f"random_number: {random_number:.2f}")
    print(random_score(random_number))
score = float(input("Enter score: "))


