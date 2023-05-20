"""Test 1"""


def details(**person_info):
    """Build a dictionary containing everything we know about a person."""
    for key, value in person_info.items():
        print(key, value)


details(name='one', age=27)
