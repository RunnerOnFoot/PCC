# 5 places that i'd like to visit.
favorite_places = ['buckingham palace', 'central park',
                   'tibet', 'pisa tower', 'hormoz island']
print(favorite_places)

# Sort the list temporarily in alphabetical order.
print(sorted(favorite_places))

# Prove the original list still exist.
print(favorite_places)

# Sort the list temporarily in reverse-alphabetical order.
print(sorted(favorite_places, reverse=True))

# Prove the original list still exist (again!).
print(favorite_places)

# Permanently reverse order of the original list.
favorite_places.reverse()
print(favorite_places)

# We use reverse() method again to return the list to its original state.
favorite_places.reverse()
print(favorite_places)

# Use the sort() method to store list permanently in alphabetical order.
favorite_places.sort()
print(favorite_places)

# Use sort() to change my list so it’s stored in reverse-alphabetical order.
favorite_places.sort(reverse=True)
print(favorite_places)
