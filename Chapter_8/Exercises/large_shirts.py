"""Exercise 8-4"""


def make_shirt(text='I love Python', size='L'):
    """Summarize the shirt that's going to be made."""
    print(f"\nI'm going to make a {size} t-shirt.")
    print(f'It will say, "{text}"')


make_shirt()
make_shirt(size='m')
make_shirt(size='xxl', text='Who Knows?')
