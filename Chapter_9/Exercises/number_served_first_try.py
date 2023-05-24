"""Exercise 9-4"""


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

    def set_number_served(self):
        """Showing the number of customers that have been served."""
        print(f"{self.number_served} customers have been served.")

    def increment_number_served(self, number):
        """Add the given amount to the number_served."""
        self.number_served += number


restaurant = Restaurant('pizzeria', 'pizza')

restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.number_served = 3
restaurant.set_number_served()

restaurant.number_served = 10
restaurant.set_number_served()

restaurant.increment_number_served(15)
restaurant.set_number_served()
