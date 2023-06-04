"""Exercise 10-14 (cleaner!)"""

from pathlib import Path
import json


def get_stored_user_info(path):
    """Get stored user info if available."""
    if path.exists():
        contents = path.read_text(encoding='utf-8')
        user_dict = json.loads(contents)
        return user_dict
    else:
        return None


def get_new_user_info(path):
    """Get information from a new user."""
    username = input("What's your name? ")
    game = input("What's your favorite game? ")
    animal = input("What's your favorite animal? ")

    user_dict = {
        'username': username,
        'game': game.lower(),
        'animal': animal.lower(),
    }

    contents = json.dumps(user_dict)
    path.write_text(contents)
    return user_dict


def greet_user():
    """Greet the user by name, and state what we know about them."""
    path = Path(r'Chapter_10\Exercises\user_info_1.json')
    user_dict = get_stored_user_info(path)

    if user_dict:
        correct = input(f"Hi, are you {user_dict['username']}? (y/n) ")
        if correct.lower() in ['y', 'yes']:
            print(f"Welcome back, {user_dict['username']}!")
            print(
                f"Hope you've been playing some {user_dict['game']}.")
            print(
                f"Have you seen a {user_dict['animal']} recently? :)")
            return

    # We got a username, but it's not correct.
    #   Prompt for a new username.
    user_dict = get_new_user_info(path)
    msg = f"We'll remember you when you return, {user_dict['username']}!"
    print(msg)


greet_user()
