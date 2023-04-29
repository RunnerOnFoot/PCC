# You can also use the keys() method to find out if a particular person was polled.
# This time, let’s find out if Erin took the poll:

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# The keys() method isn’t just for looping:
# it actually returns a sequence of all the keys.
print(favorite_languages.keys())
