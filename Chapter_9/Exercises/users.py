"""Exercise 9-3"""


class User:
    """A class representing a user."""

    def __init__(self, first_name, last_name, age,
                 job, favorite_color, location) -> None:
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.job = job
        self.favorite_color = favorite_color
        self.location = location.title()

    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Job: {self.job}")
        print(f"  Favorite color: {self.favorite_color}")
        print(f"  Location: {self.location}")

    def greet_user(self):
        """Display personalized greeting to the user."""
        fullname = f"{self.first_name} {self.last_name}"
        print(f"\nHello {fullname} :D")


parsa = User('parsa', 'mojtabai', '33',
             'Computer Programmer', 'Blue', 'alaska')
parsa.describe_user()
parsa.greet_user()

eric = User('eric', 'wolf', '38', 'programmer', 'red', 'mexico')
eric.describe_user()
eric.greet_user()
