# Make an empty list to store people in.
people = []

# Define some people, and add them to the list.
person = {
    'first_name': 'eliza',
    'last_name': 'roth',
    'age': '25',
    'city': 'rio',
}
people.append(person)

person = {
    'first_name': 'beth',
    'last_name': 'strong',
    'age': '34',
    'city': 'denmark',
}
people.append(person)

person = {
    'first_name': 'louis',
    'last_name': 'armstrong',
    'age': '19',
    'city': 'barcelona',
}
people.append(person)

# Display all of the information in the dictionary.
for person in people:
    name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = person['age']
    city = person['city'].title()

    print(f"{name}, of {city}, is {age} years old.")
