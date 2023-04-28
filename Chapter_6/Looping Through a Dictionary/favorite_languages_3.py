# Looping Through All the Keys in a Dictionary

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

for name in favorite_languages.keys():
    print(name.title())

# another way
print("\n")
for name in favorite_languages:
    print(name.title())

# You can choose to use the keys() method
# explicitly if it makes your code easier to read,
# or you can omit it if you wish.
