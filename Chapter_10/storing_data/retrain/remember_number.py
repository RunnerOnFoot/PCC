"""Saving User-Generated Data"""

from pathlib import Path
import json

user_number = input("Give me a number: ")

path = Path(r'Chapter_10\storing_data\retrain\user_number.json')
contents = json.dumps(user_number)
path.write_text(contents, encoding='utf-8')

print("We'll remember your number when you come back!")
