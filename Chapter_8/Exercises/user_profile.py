"""Exercise 8-13"""


def build_profile(first, last, **my_info):
    """Build a dictionary containing everything we know about myself."""
    my_info['first_name'] = first
    my_info['last_name'] = last

    for key, value in my_info.items():
        my_info[key] = value.title()

    return my_info


user_profile = build_profile('ali', 'bozorgi',
                             location='Bangladesh',
                             field='math',
                             sport='swim',
                             interests='art')
print(user_profile)
