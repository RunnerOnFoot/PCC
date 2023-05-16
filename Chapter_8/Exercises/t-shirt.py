"""Exercise 8-3"""


def make_shirt(size, text):
    """Display information about t-shirt"""
    print(f"\nSize: {size.upper()}")
    print(f'Text on the t-shirt: "{text}"')


make_shirt('l', 'Hello World!')
make_shirt(text='BATMAN', size='xl')
