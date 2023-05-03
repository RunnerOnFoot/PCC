# 6-7
# Make an empty list to store people in.
people = []

# Define some people, and add them to the list.
person = {
    'first_name': 'macy',
    'last_name': 'nelson',
    'age': 24,
    'city': 'rome',
}
people.append(person)

person = {
    'first_name': 'alex',
    'last_name': 'rotten',
    'age': 37,
    'city': 'amsterdam',
}
people.append(person)

person = {
    'first_name': 'tom',
    'last_name': 'bonder',
    'age': 30,
    'city': 'texas',
}
people.append(person)

# Display all of the information in the dictionary.
for person in people:
    fullname = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = person['age']
    city = person['city'].title()

    print(f"\n{fullname}, of {city}, is {age} years old.")
