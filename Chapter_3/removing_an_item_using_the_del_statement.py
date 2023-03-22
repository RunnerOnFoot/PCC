# If you know the position of the item you want to remove from a list, you can use the del statement:

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)


del motorcycles[0]
print(motorcycles)

# You can remove an item from any position in a list using the del statement if you know its index.
# Another Exp:
print('#' * 22)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)


del motorcycles[1]
print(motorcycles)

# In both examples,
# you can no longer access the value that was removed from the list after the del statement is used!!!
