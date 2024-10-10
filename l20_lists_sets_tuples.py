#   List  = [] ordered and changeable. Duplicates OK
#   Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER

fruit = ["apple", "orange", "pineapple", "apple"]
numbers = (5, 4, 3, 1, 3)
vegetables = {"tomato", "onion", "tomato"}
cars = {0: "Tesla", 1:"BMW"}

fruit.append("tree")
fruit.remove("apple")
fruit.sort()

vegetables.add("onion")

print(fruit)
print(numbers)
print(vegetables)

