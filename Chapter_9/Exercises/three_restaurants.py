"""Exercise 9-2"""


class Restaurant:
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = f"{self.name} is open. Come on in!"
        print(f"\n{msg}")


moradi = Restaurant('moradi', 'soup')
moradi.describe_restaurant()

razeghi = Restaurant('razeghi', 'steak')
razeghi.describe_restaurant()

barsa = Restaurant('barsa', 'pizza')
barsa.describe_restaurant()
