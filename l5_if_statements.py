age = int(input("Enter your age: "))

if age >= 18:
    print("Welcome to website!")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You must be 18+ to sign up!")

response = input("Would you like food? (Y/N): ")

if response == "Y":
    print("Have some food!")
else:
    print("No food for you!")

name = input("Enter your name: ")

if name == "":
    print("You did not type in your name!")
else:
    print(f"Hello {name}")