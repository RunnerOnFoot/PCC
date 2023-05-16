"""Default Values"""


def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")


describe_pet(pet_name='willie')

# The simplest way to use this function now is to provide just a dog’s name in the function call:
# describe_pet('willie')

# To describe an animal other than a dog, you could use a function call like this:
# describe_pet(pet_name='harry', animal_type='hamster')
