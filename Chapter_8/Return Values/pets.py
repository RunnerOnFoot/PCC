"""Using a Function with a while loop"""


def describe_pet(pet_name, animal_type):
    """Display information about a pet, neatly formatted."""
    msg = f"\nI have a {animal_type}. My {animal_type}'s name is {pet_name.title()}!"
    return msg


# This is a while loop with a quit condition!
while True:
    print("\nWhat's your pet name?")
    print("(enter 'q' any time to quit)")

    p_name = input("Pet name: ")
    if p_name == 'q':
        break

    print("\nWhat kind of pet do you have?")

    a_type = input("Animal Type: ")
    if a_type == 'q':
        break

    pet_info = describe_pet(p_name, a_type)
    print(pet_info)
