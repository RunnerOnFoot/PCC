# The simplest way to add a new element to a list is to append the item to the list.
# When you append an item to a list, the new element is added to the end of the list.

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

print('######################')

# The append() method makes it easy to build lists dynamically.
# For example, you can start with an empty list and then add items to the list using a series of append() calls.
# Using an empty list, let’s add the elements 'jaguar', 'mercedes benz', and 'bmw' to the list:

cars = []
cars.append("jaguar")
cars.append("mercedes benz")
cars.append("bmw")
print(cars)

# Building lists this way is very common,
# because you often won’t know the data your users want to store in a program until after the program is running.
# To put your users in control, start by defining an empty list that will hold the users’ values.
# Then append each new value provided to the list you just created.

# practicing:
print('######################')

laptops = ['lenovo', 'asus', 'apple']
print(laptops)

laptops.append('samsung')
print(laptops)

print('######################')

phones = []
phones.append('google')
phones.append('apple')
phones.append('samsung')
phones.append('nokia')
print(phones)
