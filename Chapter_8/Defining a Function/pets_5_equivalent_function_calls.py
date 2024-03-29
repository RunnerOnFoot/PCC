"""Equivalent Function Calls"""


def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")

# ALL ARE THE SAME:
    # A dog named Willie.
    describe_pet('willie')
    describe_pet(pet_name='willie')

    # A hamster named Harry.
    describe_pet('harry', 'hamster')
    describe_pet(pet_name='harry', animal_type='hamster')
    describe_pet(animal_type='hamster', pet_name='harry')
