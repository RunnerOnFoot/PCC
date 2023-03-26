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
