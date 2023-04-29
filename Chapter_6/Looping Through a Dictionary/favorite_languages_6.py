# Looping Through a Dictionary's Keys in a Particular Order

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# This tells Python to get all the keys in the dictionary
# and sort them before starting the loop.
