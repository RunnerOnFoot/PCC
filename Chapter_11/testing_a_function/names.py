"""
This program prompts the user to enter a first name and a last name. 
It uses the get_formatted_name function from the name_function module to 
format the entered names into a neatly formatted full name. 
The user can enter 'q' at any time to quit the program.
"""

from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}.")
