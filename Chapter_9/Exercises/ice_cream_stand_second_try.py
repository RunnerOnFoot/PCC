"""Exercise 9-6 (second try)"""


class Restaurant:
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type) -> None:
        """Initialize restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = f"{self.name} is open. Come on in!"
        print(f"\n{msg}")

    def set_number_served(self, number_served):
        """Allow user to set the number of customers that have been served."""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """Allow user to increment the number of customers served."""
        self.number_served += additional_served


class IceCreamStand(Restaurant):
    """
    A class representing an ice cream stand,
    inheriting from the Restaurant class.
    """

    def __init__(self, name, cuisine_type='caramel ice cream') -> None:
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an ice cream stand.
        """
        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        """Display the flavors available."""
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")


gelato = IceCreamStand('gelato')
gelato.flavors = ['banana', 'vanilla', 'chocolate']

gelato.describe_restaurant()
gelato.show_flavors()
