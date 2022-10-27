# You can add a new element at any position in your list by using the insert() method.
# You do this by specifying the index of the new element and the value of the new item:

motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.insert(0, 'ducati')
print(motorcycles)

# we insert the value 'ducati' at the beginning of the list.
# The insert() method opens a space at position 0 and stores the value 'ducati' at that location.

# practicing:
print('#' * 22)

companies = ['microsoft', 'apple', 'hooli']

companies.insert(1, 'pied piper')
print(companies)
