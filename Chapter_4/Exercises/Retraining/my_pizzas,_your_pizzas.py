favorite_pizzas = ["special", "pepperoni", "roast beef"]

friend_pizzas = favorite_pizzas[:]

# Add a new pizza to the original list
favorite_pizzas.append("younani")

# Add a different pizza to the list "friend_pizzas"
friend_pizzas.append("honey pizza")

# Prove that you have two separate lists
print("My favorite pizzas are:")
for pizza in favorite_pizzas:
    print(pizza.title())

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza.title())
