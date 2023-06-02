"""Saving and Reading User-Generated Data (pt.1)"""

# Let’s look at an example where we prompt the user for
# their name the first time they run a program and then remember their
# name when they run the program again.
from pathlib import Path
import json

username = input("What is your name? ")

path = Path(r'Chapter_10\storing_data\username.json')
contents = json.dumps(username)
path.write_text(contents, encoding='utf-8')

print(f"We'll remember you when you come back, {username}!")
