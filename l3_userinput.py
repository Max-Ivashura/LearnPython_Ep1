def user_info():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    age += 1

    print(f"Hello, {name}!")
    print(f"You are {age} years old!")


def mad_libs():
    adjective1 = input("Enter an adjective: ")
    noun = input("Enter an noun: ")
    adjective2 = input("Enter an adjective: ")
    verb = input("Enter an verb: ")
    adjective3 = input("Enter an adjective: ")
    print(f"Today I went to a {adjective1} zoo.")
    print(f"In an exhibit, i saw {noun}")
    print(f"{noun} was {adjective2} and {verb}ing")
    print(f"I was {adjective3}")


def area_calc():
    length = float(input("Enter the length of a rectangle: "))
    width = float(input("Enter the width of a rectangle: "))

    area = length * width

    print(f"The area is: {area}cm^2")


def shopping_cart():
    item = input("What item would you like to buy?: ")
    price = float(input("What is the price?: "))
    quantity = int(input("How many would you like?: "))

    total = price * quantity

    print(f"You have bought {quantity} x {item}/s")
    print(f"Your total is: ${round(total, 2)}")

shopping_cart()
