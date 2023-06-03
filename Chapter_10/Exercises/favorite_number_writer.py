"""Exercise 10-11"""

from pathlib import Path
import json

user_favorite_number = input("What's your favorite number? ")

path = Path(r'Chapter_10\Exercises\favorite_number.json')
contents = json.dumps(user_favorite_number)
path.write_text(contents, encoding='utf-8')
print("We'll remember your number when you come back!")
