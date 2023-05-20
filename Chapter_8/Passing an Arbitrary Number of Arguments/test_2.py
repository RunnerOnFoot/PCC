"""Test 2"""


def build_profile(first, last, *jobs, **user_info):
    """Mixing positional, Arbitrary Arguments, Arbitrary Keyword Arguments"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    user_info['jobs'] = jobs
    return user_info


user_profile = build_profile('alex', 'armstrong',
                             'programmer', 'musician',
                             location='rasht', sport='runner',
                             interests='art')
print(user_profile)
