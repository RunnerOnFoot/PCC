"""Saving and Reading User-Generated Data (pt.2)"""
# let’s write a new program that greets a user
# whose name has already been stored.
from pathlib import Path
import json

path = Path(r'Chapter_10\storing_data\username.json')
contents = path.read_text(encoding='utf-8')
username = json.loads(contents)

print(f"Welcome back, {username}!")
