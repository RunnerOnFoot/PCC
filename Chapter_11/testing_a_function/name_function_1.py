"""
A simple function that takes in a first, middle and last name,
and returns a neatly formatted full name.
"""


def get_formatted_name(first, middle, last):
    """Generate a neatly formatted full name."""
    full_name = f"{first} {middle} {last}"
    return full_name.title()
