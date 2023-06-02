"""Saving and Reading User-Generated Data (pt.1)"""

from pathlib import Path
import json

username = input("what is your name? ")
username = username.title()

path = Path(r'Chapter_10\storing_data\retrain\username.json')
contents = json.dumps(username)
path.write_text(contents, encoding='utf-8')

print(f"We'll remember you when you come back, {username}!")
