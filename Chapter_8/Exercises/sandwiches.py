"""Exercise 8-12"""


def make_sandwich(*items):
    """Summarize the pizza we are about to make."""
    print("\nMaking Your Perfect Sandwich:")
    for item in items:
        print(f"  ...adding {item} to your sandwich.")
    print("Your sandwich is ready :D")


make_sandwich('pepper', 'salt', 'salad', 'beef')
make_sandwich('onion', 'lemon', 'chicken')
make_sandwich('red pepper', 'bread', 'potato')
