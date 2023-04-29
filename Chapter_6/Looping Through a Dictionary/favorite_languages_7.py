# Looping Through All Values in a Dictionary

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

# If you are primarily interested in the values that a dictionary contains,
# you can use the values() method to return a sequence of values without any keys.
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
