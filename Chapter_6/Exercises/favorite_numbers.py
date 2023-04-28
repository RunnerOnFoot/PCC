# 6-2

favorite_numbers = {
    "amin": 5,
    "ali": 7,
    "pantea": 10,
    "bardia": 50,
    "parnian": 18,
}

for k, v in favorite_numbers.items():
    print(f"{k.title()}'s favorite number: {v}")

# another way:
print("\n")

num = favorite_numbers["amin"]
print(f"Amin's favorite number is {num}.")

num = favorite_numbers["ali"]
print(f"Ali's favorite number is {num}.")

num = favorite_numbers["pantea"]
print(f"Pantea's favorite number is {num}.")

num = favorite_numbers["bardia"]
print(f"Bardia's favorite number is {num}.")

num = favorite_numbers["parnian"]
print(f"Parnian's favorite number is {num}.")
