# The syntax for modifying an element is similar to the syntax for accessing an element in a list. To change an element,
# use the name of the list followed by the index of the element you want to change,
# and then provide the new value you want that item to have.
# For example, say we have a list of motorcycles and the first item in the list is 'honda'.
# We can change the value of this first item after the list has been created:

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# Here we define the list motorcycles, with 'honda' as the first element.
# Then we change the value of the first item to 'ducati'.
# The output shows that the first item has been changed, while the rest of the list stays the same.

# You can change the value of any item in a list, not just the first item!!!
