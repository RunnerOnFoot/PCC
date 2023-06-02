"""Saving and Reading User-Generated Data (pt.2)"""


from pathlib import Path
import json

path = Path(r'Chapter_10\storing_data\retrain\username.json')
contents = path.read_text(encoding='utf-8')
username = json.loads(contents)
print(f"Welcome back, {username}!")
