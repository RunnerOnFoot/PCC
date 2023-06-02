"""Saving and Reading User-Generated Data (combined)"""

from pathlib import Path
import json

path = Path(r'Chapter_10\storing_data\username.json')
if path.exists():
    contents = path.read_text(encoding='utf-8')
    username = json.loads(contents)
    print(f"Welcome back, {username}!")
else:
    username = input("What's your name? ")
    contents = json.dumps(username)
    path.write_text(contents, encoding='utf-8')
    print(f"We'll remember you when you come back, {username}!")
