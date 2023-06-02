"""
Let's Refactor greet_user() so it's not doing so many different tasks.
We'll start by moving the code for retrieving a stored username 
to a separate function.
"""

from pathlib import Path
import json


def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text(encoding='utf-8')
        username = json.loads(contents)
        return username
    else:
        return None


def greet_user():
    """Greet the user by name."""
    path = Path(r'Chapter_10\storing_data\username.json')
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = input("What's your name? ")
        contents = json.dumps(username)
        path.write_text(contents, encoding='utf-8')
        print(f"We'll remember you when you come back, {username}!")


greet_user()
