"""
A simple function that takes in a first, middle and last name,
and returns a neatly formatted full name. (making 'middle name' optional)
"""


def get_formatted_name(first, last, middle=''):
    "Generate a neatly formatted full name"
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()
