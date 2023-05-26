"""Exercise 9-8 (second try)"""


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
    """A user with administrative privileges."""

    def __init__(self, first_name, last_name, age,
                 job, favorite_color, location) -> None:
        """Initialize an admin."""
        super().__init__(first_name, last_name, age,
                         job, favorite_color, location)

        # Initialize an empty set of privileges.
        self.privileges = Privileges()


class Privileges:
    """A class to store an admin's privileges."""

    def __init__(self, privileges=[]) -> None:

        self.privileges = privileges

    def show_privileges(self):
        """Display the privileges this administrator has."""
        if self.privileges:
            print("\nPrivileges:")
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("- This user has no privileges!")


omid = Admin('omid', 'moradi', '30', 'programmer', 'orange', 'alaska')
omid.describe_user()

omid.privileges.show_privileges()

print("\nAdding privileges...")
omid_privileges = ['can add post', 'can delete post', 'can ban user',
                   'can un-ban user', 'can add comments', 'can edit comments',
                   'can delete comments', 'can reset passwords',
                   'can moderate discussions', 'can suspend accounts',]

omid.privileges.privileges = omid_privileges
omid.privileges.show_privileges()
