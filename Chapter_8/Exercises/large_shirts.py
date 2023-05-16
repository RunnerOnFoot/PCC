"""Exercise 8-4"""


def make_shirt(text='I love Python', size='L'):
    """Display information about t-shirt"""
    print(f"\nSize: {size.upper()}")
    print(f'Text on the t-shirt: "{text}"')


make_shirt()
make_shirt(size='m')
make_shirt(size='xxl', text='Who Knows?')
