# 6-8
# Make an empty list to store pets in.
pets = []

# Define some pets with the kind of animal and owners name,
# then add them to the list.
pet = {
    'animal_type': 'dog',
    'owner': 'alex',
}
pets.append(pet)

pet = {
    'animal_type': 'cat',
    'owner': 'eli',
}
pets.append(pet)

pet = {
    'animal_type': 'turtle',
    'owner': 'loki',
}
pets.append(pet)

pet = {
    'animal_type': 'monkey',
    'owner': 'robert',
}
pets.append(pet)

pet = {
    'animal_type': 'chicken',
    'owner': 'jack',
}
pets.append(pet)

# Display all of the information in the dictionary.
for pet in pets:
    animal_type = pet['animal_type'].title()
    owners_name = pet['owner'].title()

    print(f"The {animal_type} belongs to {owners_name}.")
