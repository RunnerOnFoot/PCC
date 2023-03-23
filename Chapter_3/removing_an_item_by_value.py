motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

# You can also use the remove() method to work with a value that's being removed from a list:

print('#' * 22)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

# The remove() method deletes only the first occurrence of the value you specify.
# If there’s a possibility the value appears more than once in the list,
# you’ll need to use a loop to make sure all occurrences of the value are removed.
# You’ll learn how to do this in Chapter 7.
