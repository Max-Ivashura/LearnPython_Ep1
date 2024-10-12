# --------------- main.py ---------------
from car import Car
from cup import Cup

car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Corvette", 2025, "blue", True)
car3 = Car("Charger", 2026, "yellow", True)

cup = Cup("Coffe", 0.5, False)

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

car1.drive()
car1.stop()
car3.describe()

cup.fill()
cup.drink()
cup.info()

# --------------------------------------
