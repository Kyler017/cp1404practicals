"""
CP1404/CP5632 Practical
Simple Wikipedia search app using the wikipedia package

Estimate: 30 minutes
Actual: 28 minutes
"""

import wikipedia

def main():
    print("Welcome to Wikipedia Search!")
    user_input = input("Enter page title: ").strip()

    while user_input != "":
        try:
            page = wikipedia.page(user_input, autosuggest=False)
            print(f"\n{page.title}")
            print(wikipedia.summary(user_input, sentences=2, auto_suggest=False))
            print(page.url)

        except wikipedia.exceptions.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)

        except wikipedia.exceptions.PageError:
            print('Page id "{}" does not match any pages. Try another id!'.format(user_input))
        except Exception as e:
            print("Something went wrong:", e)

        print()
        user_input = input("Enter page title: ").strip()

    print("Thank you.")

main()
