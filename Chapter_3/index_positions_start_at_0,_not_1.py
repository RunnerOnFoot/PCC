# Python considers the first item in a list to be at position 0, not position 1.
# This is true of most programming languages,
# and the reason has to do with how the list operations are implemented at a lower level.
# If you’re receiving unexpected results, ask yourself if you’re making a simple but common off-by-one error.
# The second item in a list has an index of 1. Using this counting system,
# you can get any element you want from a list by subtracting one from its position in the list. For instance,
# to access the fourth item in a list, you request the item at index 3.

from time import process_time_ns


bicycles = ['trek', 'connondale', 'redline', 'specialized']
print(bicycles[1])
print(bicycles[3])

print("##########################")

# Python has a special syntax for accessing the last element in a list. If you ask for the item at index -1,
# Python always returns the last item in the list:
print(bicycles[-1])
# This code returns the value 'specialized'. This syntax is quite useful,
# because you’ll often want to access the last items in a list without knowing exactly how long the list is.
# This convention extends to other negative index values as well.
# The index -2 returns the second item from the end of the list,
# the index -3 returns the third item from the end, and so forth.
