"""Exercise 10-12"""

from pathlib import Path
import json

path = Path(r'Chapter_10\Exercises\favorite_number.json')

try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    favorite_number = input("What's your favorite number? ")
    contents = json.dumps(favorite_number)
    path.write_text(contents, encoding='utf-8')
    print("We'll remember your favorite number when you come back!")
else:
    favorite_number = json.loads(contents)
    print(f"Here is your favorite number: '{favorite_number}'")
