"""Exercise 9-7"""


class User:
    """A class representing a user."""

    def __init__(self, first_name, last_name, age,
                 job, favorite_color, location) -> None:
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.job = job.title()
        self.favorite_color = favorite_color.title()
        self.location = location.title()
        self.login_attempts = 0

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

    def increment_login_attempts(self):
        """Increments the value of login_attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets the value of login_attempts to 0."""
        self.login_attempts = 0


class Admin(User):
    """Represent an admin."""

    def __init__(self, first_name, last_name, age,
                 job, favorite_color, location) -> None:
        """Initialize an admin."""
        super().__init__(first_name, last_name, age,
                         job, favorite_color, location)
        self.privileges = []

    def show_privileges(self):
        """lists the administrator's set of privileges."""
        print("\nHere's the list of administrator's privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


parsa = Admin('parsa', 'moradi', '30', 'programmer', 'orange', 'alaska')

parsa.privileges = ['can add post', 'can delete post', 'can ban user',
                    'can un-ban user', 'can add comments', 'can edit comments',
                    'can delete comments']
parsa.show_privileges()
