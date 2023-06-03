"""Exercise 10-11"""

from pathlib import Path
import json

path = Path(r'Chapter_10\Exercises\favorite_number.json')
contents = path.read_text(encoding='utf-8')
favorite_number = json.loads(contents)
print(f"I know your favorite number! It's '{favorite_number}'.")
