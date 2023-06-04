"""
A simple function that takes in a first and last name,
and returns a neatly formatted full name.
"""


def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    full_name = f"{first} {last}"
    return full_name.title()
