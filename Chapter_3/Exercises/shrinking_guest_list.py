guests = ['sepide', 'aram', 'hossein', 'pantea', 'bardia']
print(guests)

# Pantea can't make it! Let's invite Mehriyna instead.
del guests[3]
guests.insert(3, 'mehriyna')
print(guests)

# Print the invitations again.
name = guests[0].title()
print(
    f"\nHello {name}, we would be happy to have you at our house for dinner at 8 o'clock.")

name = guests[1].title()
print(
    f"\nHello {name}, we would be happy to have you at our house for dinner at 8 o'clock.")

name = guests[2].title()
print(
    f"\nHello {name}, we would be happy to have you at our house for dinner at 8 o'clock.")

name = guests[3].title()
print(
    f"\nHello {name}, we would be happy to have you at our house for dinner at 8 o'clock.")

name = guests[4].title()
print(
    f"\nHello {name}, we would be happy to have you at our house for dinner at 8 o'clock.")

# We got a bigger table, so let's add some more people to the list.

guests.insert(0, 'amin')
guests.insert(4, 'aida')
guests.append('helia')

print(guests)

# Print the new set of invitations.
name = guests[0].title()
print(
    f"Hello {name}, we would be happy to have you at our house for dinner at 8 o'clock")

name = guests[1].title()
print(
    f"Hello {name}, we would be happy to have you at our house for dinner at 8 o'clock")

name = guests[2].title()
print(
    f"Hello {name}, we would be happy to have you at our house for dinner at 8 o'clock")

name = guests[3].title()
print(
    f"Hello {name}, we would be happy to have you at our house for dinner at 8 o'clock")

name = guests[4].title()
print(
    f"Hello {name}, we would be happy to have you at our house for dinner at 8 o'clock")

name = guests[5].title()
print(
    f"Hello {name}, we would be happy to have you at our house for dinner at 8 o'clock")

name = guests[6].title()
print(
    f"Hello {name}, we would be happy to have you at our house for dinner at 8 o'clock")

name = guests[7].title()
print(
    f"Hello {name}, we would be happy to have you at our house for dinner at 8 o'clock")


# Oh no, the table won't arrive on time! I can invite only two people for dinner.
print('#' * 22)

deleted_guest = guests.pop()
print(
    f"Sorry {deleted_guest.title()}, there's no room at the table.")

deleted_guest = guests.pop()
print(
    f"Sorry {deleted_guest.title()}, there's no room at the table.")

deleted_guest = guests.pop()
print(
    f"Sorry {deleted_guest.title()}, there's no room at the table.")

deleted_guest = guests.pop()
print(
    f"Sorry {deleted_guest.title()}, there's no room at the table.")

deleted_guest = guests.pop()
print(
    f"Sorry {deleted_guest.title()}, there's no room at the table.")

deleted_guest = guests.pop()
print(
    f"Sorry {deleted_guest.title()}, there's no room at the table.")

print(guests)

# There should be two people left. Let's invite them.
name = guests[0].title()
print(f"Hello again {name}, you're still invited to dinner :)")

name = guests[1].title()
print(f"Hello again {name}, you're still invited to dinner :)")

# Empty out the list.
del guests[0]
del guests[0]

# Prove the list is empty.
print(guests)
