# ---------- second.py ----------
# This file should run only standalone

from first import *


def favorite_drink(drink):
    print(f"Your favorite drink is {drink}")


print("This is script2")
favorite_food("sushi")
favorite_drink("coffee")
print('Goodbye!')
